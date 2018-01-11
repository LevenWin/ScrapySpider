# -*- coding: utf-8 -*-
# Author: leven

from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from bole.utils import RedisTool

defaultencoding = 'utf-8'

class BoloTopicSpider(RedisSpider):
    name = 'boleTopic'
    redis_key = 'boleTopic_start_urls'
    def parse(self, response):
        print('### 话题列表 开始爬取:',response.url)
        topics = response.xpath("//h3[@class='p-tit']/a/@href").extract()[1:]
        if isinstance(topics,list) and (len(topics) > 0):
            RedisTool.insertDetailTopic(topics)
        nextUrl = response.xpath("//li[@id='pagination-next-page']/a/@href").extract_first()
        if nextUrl and isinstance(nextUrl,str):
            RedisTool.getConnectRedis().lpush(self.redis_key, nextUrl)





