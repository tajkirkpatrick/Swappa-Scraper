# -*- coding: utf-8 -*-
import scrapy
from ..items import PhoneItem
import re


class DiscountSpider(scrapy.Spider):
    name = 'discount'
    start_urls = ['https://swappa.com/mobile/buy/oneplus-7-pro/unlocked']

    def parse(self, response):
        swappa_domain = "https://swappa.com"

        try:
            for row in response.xpath('//*[@id="listing_previews"]/div'):
                phone = PhoneItem()
                phone["name"] = str(response.xpath(
                    '//*[@id="section_billboard"]/div/div[2]/div[3]/h1/text()').get().strip())
                phone["description"] = re.sub(
                    r'[^\w]', ' ', row.xpath('.//a/@title').get())
                phone["condition_label"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span/text()').get()
                phone["color"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span[3]/text()').get()
                phone["ram"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span[5]/text()').get()
                phone["link"] = swappa_domain + \
                    str(row.xpath('.//a/@href').get())
                phone["price"] = float(row.xpath(
                    './/a/div/div[2]/div/div/div[2]/span/text()').get())
                phone["storage"] = row.xpath(
                    './/a/div/div[2]/div/div[1]/div/span[4]/text()').get()

                if phone["price"] <= 350.0:
                    yield phone
                else:
                    print(f"Sorry, this {phone['name']} is too expensive!")

        except Exception as e:
            print(f"Error! The program encountered {e}")
