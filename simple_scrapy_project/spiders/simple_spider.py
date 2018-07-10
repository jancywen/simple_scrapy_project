# -*- coding: utf-8 -*-


import scrapy

class simple_spider(scrapy.Spider):

    name = 'simple_spider'

    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback= self.parse)


    def parse(self, response):

        page = response.url.split('/')[-2]
        filename = 'simple-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)

            self.log('保存文件: %s' % filename)