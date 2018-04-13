# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    body = scrapy.Field()
    title_hash = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()

    def __repr__(self):
        return "====================="
