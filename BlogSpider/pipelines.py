# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import BlogspiderItem
from tomd import Tomd
import time


class BlogspiderPipeline(object):
    def __init__(self):
        self.file_head = """---\ntitle: {}\ndate: {}\ntags:\n\t- Python\n---"""
        self.foot = "\n> 文章来源于转载, 如有疑问, 请联系我,转载地址:{} "

    def process_item(self, item, spider):
        if isinstance(item, BlogspiderItem):
            self.process_runoob(item)
        return item

    def process_runoob(self, item):
        body = item['body']
        file_title = item['title_hash']
        title = item['title']
        with open('mdfiles/{}.md'.format(file_title),
                  'w', encoding='utf-8') as file:
            tmp = time.strftime("%Y-%m-%d %X")
            file.write(self.file_head.format(title, tmp))
            file.write(Tomd(body).markdown)
            file.write(self.foot.format(item['url']))
