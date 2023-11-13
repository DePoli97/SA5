import scrapy
import time

class Test_spider(scrapy.Spider):

    name = "esa"

    start_urls = [
        # "https://www.esa.int/ESA/Our_Missions",
        # "https://www.esa.int/Applications/Observing_the_Earth/FutureEO/Aeolus",
        # "https://www.esa.int/Applications/Connectivity_and_Secure_Communications/Alphasat/Overview",
        # "https://www.esa.int/Applications/Observing_the_Earth/Altius",
        # "https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/Arctic_Weather_Satellite",
        # "https://www.esa.int/Enabling_Support/Space_Transportation/Ariane",
        "https://www.esa.int/Applications/Connectivity_and_Secure_Communications/Artemis"
        ]

    def parse(self, response):    # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []

        for mission in response.xpath("//div[@class='grid-item highlight mission']"):# For each mission element in the current page...
            # print(mission)
            name = mission.xpath(".//h3[@class='heading']/text()").get()
            
            # link = mission.xpath(".//a[contains(concat( ' ', @class, ' ' ), concat( ' ', 'card', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'highlight', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'mission', ' ' ))]/@href").get()
            # if link is not None and link.startswith("/"):
            #     link = "https://www.esa.int" + link
            #     next_pages.append(link)
            # yield {'mission_name': name
            #        , 'mission_link' : link
            #        }
            # time.sleep(1)
        mission_name = response.xpath("//h1[@class='heading']/text()").get()
        mission_descrition = response.xpath("//div[@class='mission-intro']//p/text()").get()
        yield {'mission_name': mission_name,
                'mission_descrition' : mission_descrition,
                # 'mission_link' : link
        }
        # time.sleep(5)
        # for page in next_pages:
        #     yield response.follow(page, callback=self.parse)
        #     # break