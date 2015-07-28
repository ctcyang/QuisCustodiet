'''
  @author: Josh Snider
  To run, use `scrapy runspider crawler.py`.
'''
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider
from scrapy.http import Request
from sets import Set

DOMAIN = 'tvtropes.com'
URL = 'http://' + DOMAIN

class TropesSpider(Spider):
    name = DOMAIN
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]
    crawled = Set([])

    def isValid(self, url):
      valid = (url not in self.crawled and
        DOMAIN in url and 'mailto' not in url and
        '?action' not in url and 'php?' not in url)
      return valid

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for url in hxs.select('//a/@href').extract():
            if not url.startswith('http'):
                url = URL + url
            if self.isValid(url):
              print url
              self.crawled.add(url)
              yield Request(url, callback=self.parse)

    #custom_settings = { "DOWNLOAD_DELAY": 2,
	#				    "CONCURRENT_REQUESTS_PER_DOMAIN": 2}
