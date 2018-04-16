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


class ShiBor(Spider):
    name = 'shibor'
    
    def start_requests(self):
        url = 'http://www.shibor.org/shibor/web/AllShibor.jsp'