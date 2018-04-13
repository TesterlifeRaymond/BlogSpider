"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/13 下午3:30
@File: crawl_topic.py
@License: MIT
"""

from scrapy import Spider, Request
from ..items import BlogspiderItem
from hashlib import md5


class CrawlerTopic(Spider):
    name = "crawl"
    allowed_domains = ["jianshu.com"]
    
    def start_requests(self):
        start_urls = "https://www.jianshu.com/p/047b4dd3f911"
        yield Request(start_urls, callback=self.parse, headers=self.settings['HEADERS'])

    def parse(self, response):
        urls = response.xpath('//*[@class="show-content-free"]/p/a/@href').extract()
        for url in urls:
            if 'link' in url:
                continue
            yield Request(url, callback=self.get_page_info, headers=self.settings['HEADERS'])
            
    def get_page_info(self, response):
        item = BlogspiderItem()
        title = response.xpath('//*[@class="title"]/text()').extract()[0]
        title_hash = md5(title.encode()).hexdigest()
        category = 2
        body = response.xpath('//*[@class="show-content"]').extract()[0]
        item['title'] = title
        item['title_hash'] = title_hash
        item['body'] = body
        item['url'] = response.url
        item['category'] = category
        yield item
