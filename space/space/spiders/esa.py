import scrapy
import time

class Test_spider(scrapy.Spider):

    name = "esa"

    start_urls = [
        "https://www.esa.int/ESA/Our_Missions"
        ]
    

    def parse(self, response):    # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []

        for mission in response.xpath("//div[@class='grid-item highlight mission']"):# For each mission element in the current page...
            name = mission.xpath(".//h3[@class='heading']/text()").get()

            link = mission.xpath(".//a[contains(concat( ' ', @class, ' ' ), concat( ' ', 'card', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'highlight', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'mission', ' ' ))]/@href").get()

            if link is not None and link.startswith("/"):
                link = "https://www.esa.int" + link
                next_pages.append(link)

        mission_name = response.xpath("//h1[@class='heading']/text()").get()
        mission_descrition = response.xpath("//div[@class='mission-intro']//p/text()").get()

        yield {'mission_name': mission_name,
                'mission_descrition' : mission_descrition,
                'mission_page' : response.url
        }
        for page in next_pages:
            yield response.follow(page, callback=self.parse)
