import scrapy

from scrapy.loader import ItemLoader
from quotescrawler.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = "quote_home_page"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = []
        for quote in response.xpath('/html/body/div/div[2]/div[1]/div'):

            item_loaded = ItemLoader(item=QuoteItem(), response=response)
            item_loaded.add_value('text', quote.xpath('.//span[1]/text()').get())
            item_loaded.add_value('author', quote.xpath('.//span[2]/small/text()').get())

            item_loaded = item_loader.load_item()

            quotes.append(item_loaded)

        self.log(quotes)
