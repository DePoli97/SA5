import scrapy

class Test_spider(scrapy.Spider):
    name = "spaceflight_now"

    start_urls = ["https://spaceflightnow.com/category/news-archive/page/1/"]

    def parse(self, response):

        next_pages = []

        page_numbers = response.css('a.page-numbers')
        if page_numbers[-1].css('a::text').get() == "»":
            next_page = page_numbers[-1].css('a::attr(href)').get()
            next_pages.append(next_page)

        for article in response.css('article.mh-posts-list-item'):

            yield {
                'title': article.css('div header h3 a::text').get().strip(),
                'link': article.css('div header h3 a::attr(href)').get(),
                'date': article.css('div header div span a::text').get(),
                'description': article.css('div div div p::text').get()
            }

        for page in next_pages:
            yield response.follow(page, callback=self.parse)