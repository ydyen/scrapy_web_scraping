import scrapy

class HorseSpider(scrapy.Spider):
    #name of file to be executed 'scrapy crawl Whirlaway'
    name = 'ike'

    #request and how to follow links
    def start_requests(self):
        urls = ['http://treehouse-projects.github.io/horse-land/index.html',
            'http://treehouse-projects.github.io/horse-land/mustang.html']

        #loops through and returns each url link and parse it
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    #parses the html files and copied
    def parse(self, response):
        url = response.url
        page = url.split('/')[-1]
        filename = 'horses-%s' % page
        print('URL is: {}'.format(url))
        with open(filename, 'wb') as file:
            file.write(response.body)
        print('Saved file %s' % filename)