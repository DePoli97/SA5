import time
import scrapy

class Test_spider(scrapy.Spider):

    name = "nasa"

    start_urls = [
        "https://www.nasa.gov/missions/"
                  ]

    def parse(self, response):    # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []

        for mission in response.xpath("//div[@class='grid-item highlight mission']"):# For each mission element in the current page...
            # print(mission)
            # name = mission.xpath(".//h3[@class='heading']/text()").get()

            link = mission.xpath(".//a[contains(concat( ' ', @class, ' ' ), concat( ' ', 'card', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'highlight', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'mission', ' ' ))]/@href").get()
            if link is not None and link.startswith("/"):
                next_pages.append("https://www.nasa.gov" + link)
            # yield {'mission_name': name
            #        , 'mission_link' : link
            #        }
            time.sleep(1)
        for page in next_pages:
            yield response.follow(page, callback=self.parse)
            # break