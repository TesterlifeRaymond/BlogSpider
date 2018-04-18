"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/16 下午5:25
@File: jianshu_everyday.py
@License: MIT
"""

import os
import json
from hashlib import md5
from scrapy import Spider, Request, FormRequest
from ..items import BlogspiderItem


class JianShu(Spider):
    name = "day"
    base_url = 'https://www.jianshu.com/p/'
    
    def start_requests(self):
        url = "https://www.jianshu.com/search?q=python&page=1&type=note"
        headers = self.settings['HEADERS']
        del headers['Referer'], headers['Origin']
        yield Request(url, callback=self.parse, dont_filter=True,
                      headers=headers)
    
    def parse(self, response):
        url = "https://www.jianshu.com/search/do?q=python&type=note&page=1&order_by=default&time_range=a_day"
        csrf = response.xpath('//*[@name="csrf-token"]/@content').extract()[0]
        headers = self.settings['DAY_HEADERS']
        headers["X-CSRF-Token"] = headers["X-CSRF-Token"].format(csrf)
        yield Request(url, callback=self.parse_list, headers=headers, method="POST")
    
    def parse_list(self, response):
        result = json.loads(response.text)
        for item in result.get("entries", []):
            did = item.get('slug')
            if not did:
                continue
            url = self.base_url + did
            yield Request(url, self.get_page_info, headers=self.settings['HEADERS'])

    def get_page_info(self, response):
        item = BlogspiderItem()
        item['publish_time'] = response.xpath('//*[@class="publish-time"]/text()').extract()[0]
        title = response.xpath('//*[@class="title"]/text()').extract()[0]
        title_hash = md5(title.encode()).hexdigest()
        body = response.xpath('//*[@class="show-content"]').extract()[0]
        item['title'] = title
        item['title_hash'] = title_hash
        item['body'] = body
        item['url'] = response.url
        item['category'] = 0
        yield item