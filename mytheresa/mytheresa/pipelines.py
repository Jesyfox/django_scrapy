# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from trophy_viewer.tasks import add_to_db
from scrapy import signals

NUMBER_OF_ITEMS_TO_SEND = 5


class MytheresaPipeline(object):
    def __init__(self, crawler):
        self.item_array = []

    def send_to_db(self):
        add_to_db.delay(self.item_array)
        self.item_array = []

    def process_item(self, item, spider):
        dict_item = dict(item)
        dict_item.update(category=spider.name)
        self.item_array.append(dict_item)

        if len(self.item_array) == NUMBER_OF_ITEMS_TO_SEND:
            self.send_to_db()

        return item

    @classmethod
    def from_crawler(cls, crawler):
        ins = cls(crawler.settings)
        crawler.signals.connect(ins.spider_finished, signal=signals.spider_idle)
        return ins

    def spider_finished(self, **kwargs):
        if self.item_array:
            self.send_to_db()

