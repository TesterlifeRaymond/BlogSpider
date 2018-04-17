"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/16 下午12:02
@File: shibor.py
@License: MIT
"""
import time
from scrapy_splash import SplashRequest
from scrapy import Request, Spider
from ..items import ShiBorItem


class ShiBor(Spider):
    name = 'shibor'
    
    def start_requests(self):
        url = 'http://www.shibor.org/shibor/Shibor.do?date={}'.format(time.strftime("%Y-%m-%d"))
        yield Request(url, self.parse)
    
    def parse(self, response):
        item = ShiBorItem()
        item['html'] = response.text
        yield item