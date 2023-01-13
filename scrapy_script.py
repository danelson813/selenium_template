import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 

class TestSpider(scrapy.Spider):
    name = 'test'
    
    custom_settings = { 'DOWNLOAD_DELAY': 1 }

    def start_requests(self):
        df = pd.read_csv("book_info.csv", header=None) 
        urls = df[0].values
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        name = response.xpath('//h1/text()').get().strip()
        author = response.xpath("//a[@class='authorName']/span/text()").get().strip()
        auth_link = response.xpath("//a[@class='authorName']/@href").get().strip()
        try:
            book_format = response.xpath("//div[@id='details']/div/span//text()").get().strip()
        except AttributeError:
            book_format = 'na'
        try:
            num_pages = response.xpath("//div[@id='details']/div/span[2]/text()").get().strip()
        except AttributeError:
            num_pages = 'na'
        try:
            pub = response.xpath("//div[@class='row'][2]/text()").get().strip().replace('\n', ' ').replace('         ', ' ')
        except AttributeError:
            pub = 'na'
        result = {
            'title': name,
            'author': author,
            'author_link': auth_link,
            'book_format': book_format,
            'number_pages': num_pages,
            'published': pub
        }
        yield result
        
        


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'book_information.csv'
    })
    process.crawl(TestSpider)
    process.start()

