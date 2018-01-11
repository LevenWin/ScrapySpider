# -*- coding: utf-8 -*-
# Author: leven

from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from bole.utils import RedisTool
from bole.items import BoleTopicItem
defaultencoding = 'utf-8'

class BoloTopicDetailSpider(RedisSpider):
    name = 'boleDetailTopic'
    custom_settings = {
        'ITEM_PIPELINES': {
            'bole.pipelines.BoloTopicPipeline': 300,
            'bole.pipelines.BoloTopicDuplicatedPipeline': 200

        }
    }

    redis_key = 'boleDetailTopic_start_urls'

    def parse(self, response):
        print('### 话题详细 开始爬取:',response.url)

        item = BoleTopicItem()

        item['title'] = response.xpath("//h1[@class='p-tit-single']/text()").extract_first().strip()
        item['publicTime'] = response.xpath("//li[@class='media']//p[@class='p-meta']/span[1]/text()").extract_first().strip()

        commentsCount = response.xpath("//li[@class='media']//p[@class='p-meta']/span[3]/text()").extract_first()
        if isinstance(commentsCount,str):
            commentsCount = commentsCount.strip('评论 ')
        else:
            commentsCount = '0'
        item['commentsCount'] = commentsCount

        item['users'] = response.xpath("//a[contains(@href, 'http://www.jobbole.com/members/')]/@href").extract()
        setUsers = set(item['users'])
        item['users'] = list(setUsers)

        yield item


#
