"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/13 上午11:17
@File: jianshu.py
@License: MIT
"""

from hashlib import md5
from scrapy import Spider, Request
from ..items import BlogspiderItem


class JianShu(Spider):
    name = "jianshu"
    base_url = 'http://www.jianshu.com'
    
    def start_requests(self):
        start_urls = ['https://www.jianshu.com/c/22f2ca261b85',
                      'https://www.jianshu.com/c/22f2ca261b85?order_by=top']
        for item in start_urls:
            yield Request(item, callback=self.parse, headers=self.settings['HEADERS'])

    def parse(self, response):
        result = response.xpath('//*[@class="note-list"]/li/a')
        for item in result:
            yield Request(self.base_url + item.xpath('@href').extract()[0],
                          callback=self.get_page_info,
                          headers=self.settings['HEADERS'])

    def get_page_info(self, response):
        item = BlogspiderItem()
        title = response.xpath('//*[@class="title"]/text()').extract()[0]
        title_hash = md5(title.encode()).hexdigest()
        body = response.xpath('//*[@class="show-content"]').extract()[0]
        item['title'] = title
        item['title_hash'] = title_hash
        item['body'] = body
        item['url'] = response.url
        yield item
