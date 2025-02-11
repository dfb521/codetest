import csv
import time
import os


class CsvPipeline:
    def __init__(self):
        self.file = None
        self.writer = None
        self.filename = f"bond_data_{time.strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    def open_spider(self, spider):
        # 创建并打开CSV文件
        self.file = open(self.filename, 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)

        # 写入表头
        self.writer.writerow(('ISIN', 'Bond_Code', 'Issuer', 'Bond_Type', 'Issue_Date', 'Latest_Rating'))

    def close_spider(self, spider):
        # 关闭CSV文件
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        # 将每个项目的字段写入CSV文件
        self.writer.writerow((
            item.get('ISIN', ''),
            item.get('Bond_Code', ''),
            item.get('Issuer', ''),
            item.get('Bond_Type', ''),
            item.get('Issue_Date', ''),
            item.get('Latest_Rating', '')
        ))
        return item