# -*- coding: utf-8 -*-
# Author: leven

from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from bole.utils import RedisTool
from bole.items import BoleUserItem

defaultencoding = 'utf-8'

class BoloUserSpider(RedisSpider):
    name = 'boleUser'
    redis_key = 'user'
    custom_settings = {
        'ITEM_PIPELINES': {
            'bole.pipelines.BoloUserPipeline': 200
        }
    }
    def parse(self, response):

        item = BoleUserItem()
        item['url'] = response.url
        item['imageUrl']= response.xpath("//span[@class='profile-img']//img/@src").extract_first()
        item['name'] = response.xpath("//span[@class='profile-title']/a/text()").extract_first()
        item['jobDesc'] = ''.join(response.xpath("//div[contains(@class,'member-profile')]/div/text()").extract()).strip()
        item['weibo'] = response.xpath("//a[@title='微博主页']/@href").extract_first()
        item['userSite'] = response.xpath("//a[@title='我的网站']/@href").extract_first()
        item['github'] = response.xpath("//a[@title='GitHub主页']/@href").extract_first()
        if item['weibo'] == None:
            item['weibo'] = ''

        if item['userSite'] == None:
            item['userSite'] = ''

        if item['github'] == None:
            item['github'] = ''

        item['userInfor'] = response.xpath("//div[@class='profile-bio']/text()").extract_first()

        registerTimeTemp = response.xpath("//div[contains(@class,'member-info')]//i[contains(@class,'fa-user')]/parent::*/parent::*/text()").extract_first()
        if isinstance(registerTimeTemp,str) and len(registerTimeTemp) > 0:
            item['registerTime'] = registerTimeTemp.strip('：').strip()
        else:
            item['registerTime'] = ''

        locationTemp = response.xpath("//div[contains(@class,'member-info')]//i[contains(@class,'fa-map-marker')]/parent::*/parent::*/text()").extract_first()
        if isinstance(locationTemp, str) and len(locationTemp) > 0:
            item['location'] = locationTemp.strip('：').strip()
        else:
            item['location'] = ''

        companyTemp =  response.xpath("//div[contains(@class,'member-info')]//i[contains(@class,'fa-building')]/parent::*/parent::*/text()").extract_first()
        if isinstance(companyTemp, str) and len(companyTemp) > 0:
            item['company'] = companyTemp.strip('：').strip()
        else:
            item['company'] = ''

        if len(response.xpath("//i[@title='男生']")) > 0:
            item['sex'] = 'm'
        elif len(response.xpath("//i[@title='女生']")) > 0:
            item['sex'] = 'f'
        else:
            item['sex'] = '' # 保密的性别

        yield item



