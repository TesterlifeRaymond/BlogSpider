"""
@Version: 1.0
@Project: BlogSpider
@Author: Raymond
@Data: 2018/4/17 上午11:09
@File: downfiles.py
@License: MIT
"""
from requests import Session


class ShiBorHistoryData:
    def __init__(self):
        self.enum = {
            1: "Shibor数据",
            2: "报价数据",
            3: "Shibor均值数据",
            4: "LPR数据",
            5: "LPR均值数据"
        }