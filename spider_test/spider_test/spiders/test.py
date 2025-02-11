import scrapy
import re
import json
import sys
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from spider_test.items import SpiderTestItem

class VesselsSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["iftp.chinamoney.com.cn"]
    start_urls = ["https://iftp.chinamoney.com.cn/english/bdInfo/"]



    def start_requests(self):
        data = {
            "pageNo": "1",  # 转换为字符串
            "pageSize": "15",  # 转换为字符串
            "isin": "",
            "bondCode": "",
            "issueEnty": "",
            "bondType": "100001",  # 转换为字符串
            "couponType": "",
            "issueYear": "2003",  # 转换为字符串
            "rtngShrt": "",
        }

        headers = {
            'Referer': 'https://iftp.chinamoney.com.cn/english/bdInfo/',
            'Cookie': 'AlteonP10=AYM/Wiw/F6yd0nIw8ndxFQ$$; apache=bbfde8c184f3e1c6074ffab28a313c87; ags=b168c5dd63e5c0bebdd4fb78b2b4704a; _ulta_id.ECM-Prod.ccc4=5f4f4bdfd2976a50; _ulta_ses.ECM-Prod.ccc4=c825db8389d0cc61',
            'Host': 'iftp.chinamoney.com.cn',
            'Origin': 'https://iftp.chinamoney.com.cn',
        }

        yield scrapy.FormRequest(
            url="https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN",
            dont_filter=True,
            formdata=data,
            headers=headers,  # 设置自定义请求头
            callback=self.tatalpage
        )

    def tatalpage(self, response: scrapy.http.HtmlResponse, **kwargs):
        save_text = response.json()
        total_page = save_text["data"]["total"]
        page = int(int(total_page) / 15)
        if int(total_page) % 15 != 0 and int(total_page) != 0:
            page = page + 1
        for i in range(1, page + 1):
            data = {
                "pageNo": f"{i}",  # 转换为字符串
                "pageSize": "15",  # 转换为字符串
                "isin": "",
                "bondCode": "",
                "issueEnty": "",
                "bondType": "100001",  # 转换为字符串
                "couponType": "",
                "issueYear": "2003",  # 转换为字符串
                "rtngShrt": "",
            }

        headers = {
            'Referer': 'https://iftp.chinamoney.com.cn/english/bdInfo/',
            'Cookie': 'AlteonP10=AYM/Wiw/F6yd0nIw8ndxFQ$$; apache=bbfde8c184f3e1c6074ffab28a313c87; ags=b168c5dd63e5c0bebdd4fb78b2b4704a; _ulta_id.ECM-Prod.ccc4=5f4f4bdfd2976a50; _ulta_ses.ECM-Prod.ccc4=c825db8389d0cc61',
            'Host': 'iftp.chinamoney.com.cn',
            'Origin': 'https://iftp.chinamoney.com.cn',
        }

        yield scrapy.FormRequest(
            url="https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN",
            dont_filter=True,
            formdata=data,
            headers=headers,  # 设置自定义请求头
        )

    def parse(self, response: HtmlResponse, **kwargs):
        save_text = response.json()
        value = save_text["data"]["resultList"]
        test_item = SpiderTestItem()
        for i in range(0, len(value)):
            value_list = save_text["data"]["resultList"][i]
            test_item["ISIN"] = value_list["isin"]
            test_item["Bond_Code"] = value_list["bondCode"]
            test_item["Issuer"] = value_list["entyFullName"]
            test_item["Bond_Type"] = value_list["bondType"]
            test_item["Issue_Date"] = value_list["issueStartDate"]
            test_item["Latest_Rating"] = value_list["debtRtng"]
            yield test_item
