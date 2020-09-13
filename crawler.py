from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HorseSpider(CrawlSpider):
    #name of file to be executed 'scrapy crawl Whirlaway'
    name = 'Whirlaway'

    #limits the amount of crawls

    #target link
    allowed_domains = ['treehouse-projects.github.io']

    start_urls = ['https://treehouse-projects.github.io/horse-land']

    #links allowed to crawl
    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback='parse-horses',
                  follow=True
                  )]

    def parse_horses(self, response):
        #fetched link
        url = response.url

        #fetched css selector list objects in html, xml elements
        title = response.css('title')

        #prints title and url
        print('Page URL: {}'.format(url))
        print('Page Title: {}'.format(title))

