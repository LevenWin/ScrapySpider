# -*- coding: utf-8 -*-
# Author: leven

import redis
def getConnectRedis():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    return r

def insertDetailTopic(urls):
    try:
       insertData('boleDetailTopic_start_urls',urls)
    except:
        print('### Redis insert detailTopic failed: ',urls)
def getNextDetailTopic():
    r = getConnectRedis()
    return r.rpop('boleDetailTopic_start_urls')

def insertDetailUser(urls):
    try:
        insertData('detailUser', urls)
    except:
        print('### Redis insert detailUser failed: ',urls)

def getNextDetailUser():
    r = getConnectRedis()
    r.lrem()
    return r.rpop('detailUser')

def insertData(key, datas):
    r = getConnectRedis()
    if isinstance(datas, str):
        r.lpush(key, datas)
    elif isinstance(datas, list):
        for string in datas:
            r.lpush(key, string)

def insertCrawledUrl(url):
    r = getConnectRedis()
    r.lpush('crawedlUrl',url)

def checkDuplicatedUrl(url):
    r = getConnectRedis()
    # print(r.lrange('crawedlUrl',0, -1))
    if r.lrem('crawedlUrl', url) > 0:
        r.lpush('crawedlUrl',url)
        print('#### ',url,'已经爬取过')
        return True
    else:
        r.lpush('crawedlUrl',url)
    return False

def getAllCrawedUrls():
    r = getConnectRedis()
    return r.lrange('crawedlUrl',0, -1)
def removeAllCrawedUrls():
    r = getConnectRedis()
    r.delete('crawedlUrl')


def getAllDetailUser():
    r = getConnectRedis()
    return r.lrange('detailUser',0, -1)

def getAllDetailTopic():
    r = getConnectRedis()

    return r.lrange('boleDetailTopic_start_urls',0, -1)