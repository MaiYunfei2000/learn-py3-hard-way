# FROM [Scrapy Tutorial — Scrapy 2.3.0 documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)

import scrapy

# the code for the first Spider

class QuotesSpider(scrapy.Spider):
    # identifies the Spider. It must be unique within a project, that is, you can’t set the same name for different Spiders.
    name = "quotes"
    
    # must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
    # The parse() method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests (Request) from them.
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

# To put our spider to work, go to the project’s top level directory and run:
#
# `scrapy crawl quotes`
#
# check the files in the current directory. You should notice that two new files have been created: quotes-1.html and quotes-2.html, with the content for the respective URLs, as our parse method instructs.