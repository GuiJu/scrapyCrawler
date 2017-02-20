import scrapy
from WandoujiaCrawler.items import App
from WandoujiaCrawler.items import Quote


class socialAppCrawler(scrapy.Spider):
    name = "socialAppCrawler"

    def start_requests(self):
        urls = [
            "http://www.wandoujia.com/apps",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseCategory)

    def parseCategory(self, response):
        for pageUrl in response.css('li.parent-cate a::attr(href)').extract():
            yield scrapy.Request(url=pageUrl, callback=self.parse)
            # yield scrapy.Request(url=pageUrl, callback=self.parse, meta={'proxy': 'http://proxy.asec.buptnsrc.com:8001'})

    def parse(self, response):
        for app in response.css('li.card'):
            item = App()
            item['name'] = app.css('div.app-desc h2 a::text').extract_first(),
            item['downloadTimes'] = app.css('div.app-desc div.meta span::text').extract_first(),
            item['size'] = app.xpath('//div[@class="app-desc"]/div/span[3]/text()').extract_first(),
            yield item

        next_pages = response.css('div.page-wp a::attr(href)').extract()
        for page in next_pages:
            yield scrapy.Request(url=page, callback=self.parse)


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = Quote()
            item['text'] = quote.css('span.text::text').extract_first(),
            item['author'] = quote.css('span small::text').extract_first(),
            item['tags'] = quote.css('div.tags a.tag::text').extract(),
            yield item
