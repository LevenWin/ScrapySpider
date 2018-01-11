# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    time = scrapy.Field()
    image = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    pass

class BoleTopicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publicTime = scrapy.Field()
    commentsCount = scrapy.Field()
    users = scrapy.Field()
    pass


class BoleUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    imageUrl = scrapy.Field()
    sex = scrapy.Field()
    weibo = scrapy.Field()
    github = scrapy.Field()
    userSite = scrapy.Field()
    userInfor = scrapy.Field()
    jobDesc = scrapy.Field()
    registerTime = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()








