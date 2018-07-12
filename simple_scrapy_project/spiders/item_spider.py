# -*- coding: utf-8 -*-


"""

    链接简写

"""

import scrapy


class ItemSpider(scrapy.Spider):
    name = 'item_spider'
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css('div.quote')[3]

        text = mingyan.css('.text::text').extract_first()
        author = mingyan.css('.author::text').extract_first()
        tags = mingyan.css('.tags .tag::text').extract()
        tags = ','.join(tags)

        fileName = '%s-语录.txt' % author
        f = open(fileName, 'a+')
        f.write(text)
        f.write('\n')
        f.write('标签: %s' % tags)
        f.close()





class ItemsSpider(scrapy.Spider):
    name = 'items_spider'
    start_urls = ["http://lab.scrapyd.cn/"]

    def parse(self, response):

        maingyan = response.css('div.quote')

        for m in maingyan:

            text = m.css('.text::text').extract_first()
            author = m.css('.author::text').extract_first()
            tags = m.css('.tags .tag::text').extract()
            tags = ','.join(tags)

            fileName = '%s-语录.txt' % author
            with open(fileName, 'a+') as f:
                f.write(text)
                f.write('\n')
                f.write('标签: ' + tags)
                f.write('\n--------\n')
                f.close()