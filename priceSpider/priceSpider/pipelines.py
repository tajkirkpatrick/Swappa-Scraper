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
        listing_num = 1

        if len(products_arr) != 0:
            for item in products_arr:
                with open(f'{item[0]}.txt', 'w') as fp:
                    fp.write(str(
                        f"Alert! Check on your [ {item[0]} ] at Swappa\n\npriceSpider found:\n"))
                    for listing in item[1]:
                        fp.write("\t"+str(
                            listing_num) + f": [{listing['price']}] [{listing['condition_label']}] [{listing['color']}] {listing['item']}, with description: {listing['description']}\n\t\t{listing['link']}\n")
                        listing_num += 1
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
            if price > 700:
                for item_tuple in products_arr:
                    if item_tuple[0] == name:
                        item_tuple[1].append(item)

        if name == "OnePlus 7 Pro":
            if color != "Almond":
                for item_tuple in products_arr:
                    if item_tuple[0] == name:
                        item_tuple[1].append(item)
            return item

        # if item_name not in products_arr:
        #     print("Wasn't in there")
        # else:
        #     print("SUCCESS - HERE")

        return item

        # if item["price"] < 450:
        #     return item
        # else:
        #     return None
