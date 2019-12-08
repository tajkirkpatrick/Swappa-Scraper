# -*- coding: utf-8 -*-
import scrapy


class DiscountSpider(scrapy.Spider):
    name = 'discount'
    start_urls = ['https://swappa.com/mobile/buy/oneplus-7-pro/unlocked']

    def parse(self, response):
        count = 1
        swappa_domain = "https://swappa.com"

        try:
            for row in response.xpath('//*[@id="listing_previews"]/div'):
                description = row.xpath('.//a/@title').get()
                link = swappa_domain + str(row.xpath('.//a/@href').get())

                for tree in row.xpath('.//a/div/div'):
                    for branch in tree.xpath('.//div/div/div'):
                        price = branch.xpath('.//span/text()').get()
                # print(f"#{count} ($" + str(price) + ") " + str(description) + " " + str(link))

                yield {
                    "description": description,
                    "link": link,
                    "price": price
                }

                count += 1

        except Exception as e:
            pass
