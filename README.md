这是一个配合Hexo静态Blog使用的Spider项目
------------------------------------------
用于自动更新blog的爬虫

* Usage: 
    * 项目基于scrapy实现爬虫部分的代码
    * 在piplines中使用html2text将html页面自动转换成md文件并排版
    * 数据指纹是用文章的title_md5 来进行标注的

> 该项目主要是针对简书的Python搜索/Python相关最新/Python最热几个频道进行了日常采集,
并将文章生成后生成Hexoblog的静态页面, 所有文章中标注了文章来源, 转载声明


> Sample: [Raymond's Blog](http://testerlife.com/)

* 爬虫会每日自动采集新的文章, 生成md文件后更新blog
* 由于html转markdown可能存在未知的错误, 所以我们建议在离线生成部分应用[hint-markdown语法检查工具](https://github.com/hustcc/hint)来检查md文件是否可以生成静态页面
* 后续会持续更新, 目前没发现更多问题
