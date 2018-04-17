"""
@Version: 1.0
@Project: BlogSpider
@Author: Raymond
@Data: 2018/4/17 上午11:09
@File: downfiles.py
@License: MIT
"""
from requests import Session
from urllib.parse import parse_qsl
from multiprocessing import Process
import logging
logging.basicConfig(filename='catelina.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG,)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class FileHandler:
    """
        FileHandler
        基于Python __enter__ __exit__ 对上下文进行管理,
        通过read及write方法支持file文件同时读写的操作行为
    """
    def __init__(self, filename: str, mod: str = 'r', encoding: str ="utf-8"):
        """
            初始化类属性
        @params: filename
        @params: mod
        @params: encoding
        """
        self.filename = filename
        if mod not in ['r', 'w']:
            encoding = None
        self.file = open(filename, mod, encoding=encoding)
        self.mod = mod

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.info(f"Raise {exc_type}: {exc_val}")
        else:
            self.file.close()
            logger.info(f"close file done ..")

    def read(self):
        return self.file.read().replace('\xc8\xd5\xc6\xda', '')

    def write(self, msg, mod='a'):
        with FileHandler(self.filename, mod=mod, encoding='gb2312') as wfile:
            print(msg)
            wfile.file.writelines(msg)


class ShiBorHistoryData:
    def __init__(self):
        self.enum = {
            "Historical_Shibor_Data_": "Shibor数据",
            "Historical_Quote_Data_": "报价数据",
            "Historical_Shibor_Tendency_Data_": "Shibor均值数据",
        }
        self.start_years = 2006
        self.end_years = 2019
        self.src_path = "http://www.shibor.org/shibor/"
        self.base_url = "http://www.shibor.org/shibor/web/html/downLoad.html?" \
                        "nameNew={}&nameOld={}shiborSrc={}&downLoadPath=data"
        self.session = Session()
    
    @property
    def files(self):
        files = []
        for key, value in self.enum.items():
            for item in range(self.start_years, self.end_years):
                item = str(item)
                files.append(self.base_url.format(key + item + '.txt',
                                           value + item + '.txt&', self.src_path))
                
        for key, value in self.enum.items():
            for num in range(1, 5):
                num = str(num)
                files.append(self.base_url.format(key + "2018_" +num + '.txt',
                                           value + "2018_" + num + '.txt&', self.src_path))
        return files
    
    def download_files(self, url):
        file_name = dict(parse_qsl(url))['nameOld']
        logger.info(" [ FILE NAME ] : {} STARTED ".format(file_name))
        result = self.session.get(url).content
        file = open('../files/{}'.format(file_name), 'wb')
        file.write(result)
        file.close()
        logger.info(" [ FILE NAME ] : {} DONE".format(file_name))

    def __iter__(self):
        for item in self.files:
            yield item
    

if __name__ == '__main__':
    crawl = ShiBorHistoryData()

    # for file in crawl:
    #     process = Process(target=crawl.download_files, args=(file,))
    #     process.start()
    import os
    files = os.listdir('../files')
    for file in files:
        if "Shibor数据" not in file:
            continue
        
        with FileHandler("MakeResult.txt", 'a+', 'gb2312') as obj:
            with FileHandler('../files/{}'.format(file), 'r', 'gb2312') as reader:
                msg = reader.read().replace('日期', 'DATE')
                obj.write(msg)