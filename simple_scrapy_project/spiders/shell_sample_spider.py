# -*- coding: utf-8 -*-

"""
    在spider中启动shell来查看response

"""

import scrapy


class shell_sample(scrapy.Spider):

    name = 'shell_sample'
    start_urls = ['http://lab.scrapyd.cn/page/1/',
                  'http://lab.scrapyd.cn/page/2/']

    def parse(self, response):

        if "2" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)
