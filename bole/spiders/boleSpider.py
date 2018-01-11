# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from bole.items import BoleItem
from scrapy.http import Request
from urllib import parse
import sys
import time
class BolespiderSpider(RedisSpider):
    name = 'boleSpider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/3/']
    custom_settings = {
        'ITEM_PIPELINES': {

            'bole.pipelines.BolePipeline': 1
        }
    }


    # 发送 header，伪装为浏览器
    headers = {
        'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'cookie': "__c=1501326829; lastCity=101020100; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.20.1.20.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502948718; __c=1501326829; lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502954829; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.21.1.21.21",
        'cache-control': "no-cache",
        'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
    }
    def parse(self, response):
        item = BoleItem()
        archives = response.xpath("//div[@id='archive']/div[contains(@class,'post')]")
        for article in archives:
            item['image'] = article.xpath("div[@class='post-thumb']/a/img/@src").extract_first()
            item['title'] = article.xpath("div[@class='post-meta']/p/a/@title").extract_first()
            item['url'] = article.xpath("div[@class='post-meta']/p/a[@class]/@href").extract_first()
            item['time'] = ''.join(article.xpath("div[@class='post-meta']/p/text()").extract()).replace('·','').strip()
            item['tag'] = article.xpath("div[@class='post-meta']/p/a[@rel]/text()").extract_first()
            item['abstract'] = article.xpath("div[@class='post-meta']/span[@class]/p/text()").extract_first()
            yield item
        nextPage = response.xpath("//a[contains(@class,'next')]/@href").extract_first()
        print(nextPage)
        if nextPage:
            yield Request(url = parse.urljoin(response.url, nextPage), callback = self.parse)
        else:
            print('end')
        pass


