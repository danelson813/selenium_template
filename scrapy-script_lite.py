import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class TestSpider(scrapy.Spider):
    name = 'test'
    custom_settings = {'DOWNLOAD_DELAY': 1}

    def start_requests(self):
        start_urls = {
            'thhps://books.toscrape.com'
        }

    def parse(self, response):
        pass
        
        result = {

        }
        yield result


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.3)',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'book_information.csv'
    })
    process.crawl(TestSpider)
    process.start()
    