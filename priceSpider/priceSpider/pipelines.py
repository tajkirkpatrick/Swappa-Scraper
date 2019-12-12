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

        name = item["item"]
        price = item["price"]

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

        if name == "OnePlus 7 Pro":
            if price <= 456:
                for item_tuple in products_arr:
                    if item_tuple[0] == name:
                        item_tuple[1].append(item)


        # if item_name not in products_arr:
        #     print("Wasn't in there")
        # else:
        #     print("SUCCESS - HERE")

        return item

        # if item["price"] < 450:
        #     return item
        # else:
        #     return None
