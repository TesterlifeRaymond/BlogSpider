"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/12 下午5:53
@File: pythontab.py
@License: MIT
"""
import hashlib
from scrapy import Spider
from ..items import BlogspiderItem


class PythonTab(Spider):
    name = "pythontab"
    start_urls = ['http://www.pythontab.com/html/2018/pythonhexinbiancheng_0314/1258.html']
    
    def parse(self, response):
        page = response.xpath('//*[@id="Article"]').extract()[0]
        item = BlogspiderItem()
        item['body'] = page
        item['title_hash'] = hashlib.md5(
            response.xpath('//h1/text()').extract()[0].encode()
        ).hexdigest()
        item['title'] = response.xpath('//h1/text()').extract()[0].encode()
        item['url'] = response.url
        yield item