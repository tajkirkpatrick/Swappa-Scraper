# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pprint import pprint
import json
products_arr = []
existing_products = []


class SwappaPipeline(object):

    def open_spider(self, spider):
        print("Pipeline Opened")
        return

    def close_spider(self, spider):
        print(products_arr)
        return

    def process_item(self, item, spider):
        global products_arr
        global existing_products

        item_name = item["item"]

        if len(products_arr) == 0:
            products_arr.append((f"{item_name}", []))
            existing_products.append(item_name)

        for _ in products_arr:
            if item_name not in existing_products:
                existing_products.append(item_name)
                products_arr.append((f"{item_name}", []))
                break

        # if item_name not in products_arr:
        #     print("Wasn't in there")
        # else:
        #     print("SUCCESS - HERE")

        return item

        # if item["price"] < 450:
        #     return item
        # else:
        #     return None
