# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ISIN = scrapy.Field()
    Bond_Code = scrapy.Field()
    Issuer = scrapy.Field()
    Bond_Type = scrapy.Field()
    Issue_Date = scrapy.Field()
    Latest_Rating = scrapy.Field()

