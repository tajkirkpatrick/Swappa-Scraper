# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SwappaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item = scrapy.Field()
    description = scrapy.Field()
    condition_label = scrapy.Field()
    color = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
