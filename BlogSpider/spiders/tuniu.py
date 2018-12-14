# -*- coding: utf-8 -*-
"""
    BlogSpider
    ~~~~~~~~~~~~~~~~~

    tuniu.py

    DESC: 
    
    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018/12/14 下午3:35
"""

import os
from hashlib import md5
from scrapy import Spider, Request
from ..items import BlogspiderItem
import json
import time
from scrapy_splash import SplashRequest, SlotPolicy


class JianShu(Spider):
    name = "tuniu"
    base_url = 'http://www.jianshu.com'
    start_urls = ["http://trips.tuniu.com/travels/index/ajax-list?sortType=1&page=1&limit=20&_={}".format(int(time.time()))]

    def parse(self, response):
        rows = json.loads(response.text)['data']["rows"]
        for row in rows:
            item = BlogspiderItem()
            _id = row["id"]
            url = "http://www.tuniu.com/trips/{}".format(_id)
            item["title"] = row["name"]
            item["title_hash"] = md5(row["name"].encode()).hexdigest()
            item["publish_time"] = row["publishTime"]
            item['category'] = 3
            item["url"] = url
            # print(url)
            yield Request(url, self.parse_body, meta={"item": item})

    def parse_body(self, response):
        pattern = '//*[@class="sdk-trips-container"]'
        body = response.xpath(pattern).extract()
        if not body:
            return
        item = response.meta["item"]
        item["body"] = body[0]
        # print({"url": item["url"], "title": item["title"], "hash": item["title_hash"]})
        return item





