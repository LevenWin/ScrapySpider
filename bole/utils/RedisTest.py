# -*- coding: utf-8 -*-
# Author: leven

import redis
from bole.utils import RedisTool

# RedisTool.insertCrawledUrl('hahah')
#
# RedisTool.checkDuplicatedUrl('hahah')
# # 获取
# RedisTool.checkDuplicatedUrl('hahah4324324')

RedisTool.removeAllCrawedUrls()

arr = RedisTool.getAllCrawedUrls()
RedisTool.getConnectRedis().delete('boleDetailTopic_start_urls')
print(len(arr))
print(arr)