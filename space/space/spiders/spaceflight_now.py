import scrapy

class Test_spider(scrapy.Spider):
    name = "spaceflight_now"

    start_url = "https://spaceflightnow.com/category/news-archive/"

    def parse(self, response):

        next_pages = []

        for article in response.css('article.mh-posts-list-item'):
            yield {
                'title': article.css('div header h3 a::text').get().strip(),
                'link': article.css('div header h3 a::attr(href)').get(),
                'date': article.css('div header div span a::text').get(),
                'description': article.css('div div div p::text').get()
            }