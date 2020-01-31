# -*- coding: utf-8 -*-
import scrapy
from ..items import SwappaItem
import re


class DiscountSpider(scrapy.Spider):
    name = 'swappa'
    start_urls = ['https://swappa.com/mobile/buy/oneplus-7-pro/unlocked']
                #   'https://swappa.com/gaming/buy/xbox-one-x']

    def parse(self, response):
        swappa_domain = "https://swappa.com"

        try:
            for row in response.xpath('//*[@id="listing_previews"]/div'):
                item = SwappaItem()
                item["item"] = str(response.xpath(
                    '//*[@id="section_billboard"]/div/div[2]/div[3]/h1/text()').get().strip())
                item["description"] = re.sub(
                    r'[^\w]', ' ', row.xpath('.//a/@title').get())
                item["condition_label"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span/text()').get()
                item["color"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span[3]/text()').get()
                item["link"] = swappa_domain + \
                    str(row.xpath('.//a/@href').get())
                item["price"] = float(row.xpath(
                    './/a/div/div[2]/div/div/div[2]/span/text()').get())

                yield item

        except Exception as e:
            print(f"Error! The program encountered {e}")
