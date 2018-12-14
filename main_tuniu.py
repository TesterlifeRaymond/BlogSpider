# -*- coding: utf-8 -*-
"""
    BlogSpider
    ~~~~~~~~~~~~~~~~~

    main_tuniu.py

    DESC: 
    
    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018/12/14 下午3:36
"""

from scrapy.cmdline import execute

execute("scrapy crawl tuniu".split())