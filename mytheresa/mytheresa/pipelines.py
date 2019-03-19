# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from trophy_viewer.tasks import add_to_db

NUMBER_OF_ITEMS_TO_SEND = 1


class MytheresaPipeline(object):
    def __init__(self):
        self.item_array = []

    def process_item(self, item, spider):
        dict_item = dict(item)
        dict_item.update(category=spider.name)
        self.item_array.append(dict_item)
        if len(self.item_array) == NUMBER_OF_ITEMS_TO_SEND:
            add_to_db.delay(self.item_array)
            self.item_array = []
        return item
