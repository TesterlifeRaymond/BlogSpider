"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/16 上午10:37
@File: crawl_wechat.py
@License: MIT
"""
import time
from scrapy_splash import SplashRequest
from scrapy import Spider, Request
from hashlib import md5
from ..items import BlogspiderItem


class WeChat(Spider):
    name = "wechat"
    start_time = int(time.time() * 1000)

    def start_requests(self):
        headers = self.settings['WECHAT_HEADERS']
        headers['Referer'] = headers['Referer'].format(self.start_time)
        yield Request(headers['Referer'], callback=self.parse, headers=headers)

    def parse(self, response):
        urls = response.xpath('//*[@class="pic-list"]/ul/li/div/a/@href').extract()
        for url in urls:
            print(url)
            yield SplashRequest(url, callback=self.get_page_info)

    def get_page_info(self, response):
        item = BlogspiderItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        item['body'] = response.xpath('//*[@class="rich_media_content "]').extract()[0]
        item['title_hash'] = md5(item['title'].encode()).hexdigest()
        item['url'] = response.url
        item['category'] = 3
        yield item
