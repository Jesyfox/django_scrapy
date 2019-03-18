# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from trophy_viewer.tasks import add_to_db
import os
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytheresa_dj.settings")
django.setup()


class MytheresaPipeline(object):
    def __init__(self):
        self.item_array = []

    def process_item(self, item, spider):
        self.item_array.append(item)
        add_to_db.delay(len(self.item_array))
        return item
