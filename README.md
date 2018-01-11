使用scrapy ，scrapy-redis实现的爬虫，以mongodb为底层存储机制，利用Redis来高效率的存储多次读写的数据和去重。

### 项目依赖
  + python 3.5+
  + scrapy
  + scrapy-redis
  + pymongo
  + graphite

### 如何运行
先保证已安装相关依赖库，以及mongodb服务，redis服务已开启
- 在main文件中仅取消 `execute(['scrapy','crawl','boleTopic'])`注释，并且build main.py ，运行 `boleTopic`爬虫，爬取所有的话题链接存进redis中
- 在main文件中仅取消 `execute(['scrapy','crawl','boleDetailTopic'])`注释，并且build main.py ，运行 `boleDetailTopic`爬虫，爬取详细话题中的用户链接，存在mongodb中
- 等所有的用户链接爬取完毕后，build mongodb.py 将mongodb的用户链接存在redis当中。此时可以开启`boleUser`爬虫，获取所有的用户信息存进mongodb当中


### 去重

期间所有爬取过的链接 都会存近redis `crawedlUrl`set 当中，以达到去重的目的
