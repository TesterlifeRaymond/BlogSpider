"""
@File: runoob
@Author: Ray
@Date: 2018-04-12 11:28:07
@Version: 1.0
"""

from scrapy import Spider
import hashlib
from scrapy_splash import SplashRequest
from ..items import BlogspiderItem


class Runoob(Spider):
    name = "runoob"
    start_urls = ['http://www.runoob.com/python3/python3-tutorial.html']
    base_url = "http://www.runoob.com"

    def parse(self, response):
        """
            获取首页中全部的next page url
        @response: start_urls中起始页面的response对象
        """
        navbar_xpath = response.xpath('//*[@id="leftcolumn"]/a')
        for index, item in enumerate(navbar_xpath):
            if index == 0:
                continue
            title = item.xpath('@title').extract()[0]
            href = self.base_url + '/python3/' + item.xpath('@href').extract()[0]
            title_hash = hashlib.md5(title.encode()).hexdigest()
            meta = {
                "title": title,
                "title_hash": title_hash
            }
            yield SplashRequest(
                href, callback=self.get_content, meta=meta
            )

    def get_content(self, response):
        item = BlogspiderItem()
        result = response.xpath(
            '//*[@class="article-body"]').extract()[0].replace('\n', '')
        result = result.replace('\r', '').replace('\t', '')
        item['body'] = result
        item['title_hash'] = response.meta['title_hash']
        item['title'] = response.meta['title']
        item['url'] = response.url
        yield item
