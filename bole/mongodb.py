# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bole.utils import RedisTool

defaultencoding = 'utf-8'

class BoleDB(object):
    def __init__(self, dbSet):
        try:
            self.conn = MongoClient('127.0.0.1',27017)
            self.db = self.conn.bole
            self.dbSet = self.db[dbSet]
        except Exception as e:
            print(e)
    def inser(self,dict):
        self.dbSet.insert(dict)

    def update(self, dic, newdic):
        self.dbSet.update(dic, newdic)

    def close(self):
        self.conn.close()

    def get(self, fromIndex = 0, count = 100):
        return list(self.dbSet.find({}).skip(fromIndex).limit(count))

#
if __name__ == '__main__':

    db = BoleDB('topic')
    fromIndex = 0
    count = 100
    arr = list()
    conn = RedisTool.getConnectRedis()

    while len(arr) == count or fromIndex == 0:
        arr = db.get(fromIndex, count)
        fromIndex += count
        for item in arr:
            users = item['users']
            for user in users:
                conn.lpush('user', user)
                print(user)

    print(fromIndex, count)
