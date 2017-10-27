# -*- coding: utf-8 -*-
import scrapy


class SpidernewsSpider(scrapy.Spider):
    name = 'spiderNews'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):

        print(response.text)

