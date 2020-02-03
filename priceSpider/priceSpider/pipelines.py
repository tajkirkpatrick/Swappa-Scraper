# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pprint import pprint
from .mailbox import MailSender


products_arr = []
existing_products = []
mailman = MailSender()


class SwappaPipeline(object):

    def open_spider(self, spider):
        print("Pipeline Opened")
        return

    def close_spider(self, spider):
        emailTrigger = False

        for product in products_arr:
            if len(product[1]) != 0:
                emailTrigger = True

        if emailTrigger:
            self.webToText(products_arr)
            mailman.sendEmail()

        return

    def process_item(self, item, spider):
        global products_arr
        global existing_products

        name = item["item"]
        price = item["price"]
        color = item["color"]

        if len(products_arr) == 0:
            products_arr.append((f"{name}", []))
            existing_products.append(name)

        for _ in products_arr:
            if name not in existing_products:
                existing_products.append(name)
                products_arr.append((f"{name}", []))
                break

        if name == "Xbox One X":
            if price < 300:
                for item_tuple in products_arr:
                    if item_tuple[0] == name:
                        item_tuple[1].append(item)
            return item

        if name == "OnePlus 7 Pro":
            if color == "Almond":
                for item_tuple in products_arr:
                    if item_tuple[0] == name:
                        item_tuple[1].append(item)
            return item

        return

    def webToText(self, arr):
        listing_num = 1

        with open('swappa_web.txt', 'w') as fp:
            fp.write(str(
                f"Alert! Spider caught these in the [ {arr[0][0]}, {arr[1][0]} ] web from Swappa\n\npriceSpider potential victims:\n"))

        with open('swappa_web.txt', 'a') as fp:
            for item in arr:
                for listing in item[1]:
                    fp.write(str(listing_num) +
                             f": [{listing['item']}] [{listing['price']}] [{listing['condition_label']}] [{listing['color']}] description: {listing['description']}\n\t{listing['link']}\n\n")
                    listing_num += 1

            fp.write(
                "Note: IF item is listed in web brackets, but no listing is found. Item was scraped but no listings met criteria.")
        return
