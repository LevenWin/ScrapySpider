# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from bole.mongodb import BoleDB

class BolePipeline(object):
    def process_item(self, item, spider):
        print('bolepipeline')
        return item
    def open_spider(self,spider):
        print('open spider...')
        pass
    def close_spider(self,spider):
        print('close spider...')
        pass

class BoloTopicDuplicatedPipeline(object):
    def process_item(self, item, sipder):
        users = item['users']
        usersList = list()
        for user in users:
            shouldAdd = True
            for url in usersList:
                if user in url or url in user:
                    shouldAdd = False
                    break
            if shouldAdd:
                usersList.append(user)
        item['users'] = usersList

        return item


class BoloTopicPipeline(object):
    def __init__(self):
        self.db = BoleDB('topic')

    def open_spider(self, spider):
        pass

    def close_spider(self,spider):
        self.db.close()

    def process_item(self,item,spider):
        try:
            self.db.inser(dict(item))
        except Exception as e:
            print(e)
        return item

class BoloUserPipeline(object):
    def __init__(self):
        self.db = BoleDB('user')

    def open_spider(self, spider):
        pass

    def close_spider(self,spider):
        self.db.close()

    def process_item(self,item,spider):
        try:
            self.db.inser(dict(item))
        except Exception as e:
            print(e)
        return item


