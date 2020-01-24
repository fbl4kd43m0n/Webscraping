# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    #allowed_domains = ['www.coursera.org/browse?languages=pt']
    start_urls = ['http://www.coursera.org/browse?languages=pt/']

    def parse(self, response):
        self.log('Hello World! Scrapy Project')
