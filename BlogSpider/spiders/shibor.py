"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/16 下午12:02
@File: shibor.py
@License: MIT
"""

from scrapy_splash import SplashRequest
from scrapy import Request, Spider
from ..items import ShiBorItem


class ShiBor(Spider):
    name = 'shibor'
    
    def start_requests(self):
        url = 'http://www.shibor.org/shibor/Shibor.do?date=2018-04-17'
        yield Request(url, self.parse)
    
    def parse(self, response):
        item = ShiBorItem()
        item['html'] = response.text
        yield item