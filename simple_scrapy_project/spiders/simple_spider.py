# -*- coding: utf-8 -*-


import scrapy

# 1,创建一个类继承scrapy的子类
class simple_spider(scrapy.Spider):

    # 定义蜘蛛的名字
    name = 'simple_spider'

    # 执行scrapy的方法 爬取链接网页
    def start_requests(self):

        #定义需要爬取的网站
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #将爬取到的网页交给parse处理


    def parse(self, response):

        page = response.url.split('/')[-2]
        filename = 'simple-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)  #response.body 就是爬取的网页

            self.log('保存文件: %s' % filename)