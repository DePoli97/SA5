import scrapy


class TestSpider(scrapy.Spider):
    name = "spaceflight_now"
    start_urls = ["https://spaceflightnow.com/category/news-archive/"]

    def parse(self, response):
        next_page_link = response.css('a.next::attr(href)').get()

        for article in response.css('article.mh-posts-list-item'):
            title = article.css('div header h3 a::text').get().strip()
            article_link = article.css('div header h3 a::attr(href)').get()
            date = article.css('div header div span a::text').get()
            description = article.css('div div div p::text').get()

            yield response.follow(
                article_link,
                callback=self.parse_article,
                meta={'title': title, 'link': article_link, 'date': date, 'description': description}
            )

        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        date = response.meta['date']
        description = response.meta['description']

        body = ""
        for p in response.css('p::text'):
            body += p.get().strip() + " "

        yield {
            'title': title,
            'link': link,
            'date': date,
            'description': description,
            'body': body
        }
