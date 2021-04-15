import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        for quotes in response.css("div.quote"):
            yield {
                "text": quotes.css("span.text::text").get(),
                "author": quotes.css("small.author::text").get(),
                "tags": quotes.css("div.tags a.tag::text").getall(),
            }

