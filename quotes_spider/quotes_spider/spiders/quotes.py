from numpy import absolute, extract
import scrapy

#scrapy.Spider is a subclass
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//div[@class="quote"]') #this will generate a list
        
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').extract()[0]
            author = quote.xpath('.//span/small[@class="author"]/text()').extract()[0]
            tags = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()    
            
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }
        
        next_page_url = response.xpath('.//nav/ul[@class="pager"]/li[@class="next"]/a/@href').extract()[0]
        absolute_url = response.urljoin(next_page_url)

        yield scrapy.Request(absolute_url)
            

