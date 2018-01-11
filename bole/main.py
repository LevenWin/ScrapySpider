from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','boleTopic'])
# execute(['scrapy','crawl','boleDetailTopic'])
execute(['scrapy','crawl','boleUser'])

