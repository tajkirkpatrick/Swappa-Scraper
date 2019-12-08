# -*- coding: utf-8 -*-
import scrapy


class DiscountSpider(scrapy.Spider):
    name = 'discount'
    start_urls = ['https://https://swappa.com/mobile/buy/oneplus-7-pro/unlocked/']

    def parse(self, response):
        pass
