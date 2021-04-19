import scrapy


class GooglePlaySpider(scrapy.Spider):
    name = "google_play"
    start_urls = [
        "https://play.google.com/store/apps/details?id=com.supercell.clashofclans",
        "https://play.google.com/store/apps/details?id=com.unimob.stickman.master.shadow.premium",
    ]

    custom_settings = {
        'DEPTH_LIMIT': "5",
    }

    def parse(self, response):
        for apps in response.css("div.T4LgNb"):
            yield {
                "App Name": apps.css("h1.AHFaub span::text").get(),
                "Creator": apps.css("div.qQKdcc a::text").get(),
                "Genre": apps.css("div.qQKdcc a::text")[1].get(),
                "Rate": apps.css("div.BHMmbe::text").get(),
                "Number of Reviews": apps.css("span.EymY4b span::text").get(),
                "Price": apps.css("span.oocvOe button::text").get(),
                "Additional Info": apps.css("div.IQ1z0d span.htlgb::text").getall(),
            }

        next_pages = apps.css("div.RZEgze a.JC71ub::attr(href)").getall()
        yield from response.follow_all(next_pages, callback=self.parse)