# -*- coding: utf-8 -*-

"""
    scrapy初始化url有两种方法
    1,常量 start_urls; 并且必须定义一个方法parse()方法
    2,直接定义一个方法: start_requests()
"""

import scrapy

class simpleUrl(scrapy.Spider):


    name = 'simpleUrl'

    start_urls = ['http://lab.scrapyd.cn/page/1/',
                  'http://lab.scrapyd.cn/page/2/']

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'simpleUrl_%s.html' % page

        with open(filename, 'wb'):
            filename.write(response.body)

            self.log('保存文件 %s' % filename)