import scrapy

class TestSpider(scrapy.Spider):
    name = "spaceflight_now"
    start_urls = ["https://spaceflightnow.com/category/news-archive/"]

    def parse(self, response):
        next_page_link = response.css('a.next::attr(href)').get()

        for article in response.css('article.mh-posts-list-item'):
            article_link = article.css('div header h3 a::attr(href)').get()
            yield response.follow(article_link, callback=self.parse_article)

        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)

    def parse_article(self, response):
        yield {
            'title': response.css('div header h1::text').get().strip(),
            'link': response.url,
            'date': response.css('div header div span a::text').get(),
            'description': response.css('div div div p::text').get(),
            'body': ' '.join(response.css('article div.entry-content p::text').getall())
        }
