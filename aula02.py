import scrapy

class GilenoFilhoSpider(scrapy.Spider):
    name = 'gilenofilho'
    start_urls = ['http://www.gilenofilho.com.br']

    def parse(self, message):
        self.log('Hello World')
        self.log(response.body)


        #scrapy genspider coursera www.coursera.org/browse?languages=pt