import scrapy
import time

class Test_spider(scrapy.Spider):

    name = "esa"

    start_urls = [
        "https://www.esa.int/ESA/Our_Missions"
        ]
    

    def parse(self, response): # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []

        for mission in response.xpath("//div[@class='grid-item highlight mission']"):# For each mission element in the current page...
            # name = mission.xpath(".//h3[@class='heading']/text()").get()

            link = mission.xpath(".//a[contains(concat( ' ', @class, ' ' ), concat( ' ', 'card', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'highlight', ' ' )) and contains(concat( ' ', @class, ' ' ), concat( ' ', 'mission', ' ' ))]/@href").get()

            if link is not None and link.startswith("/"):
                link = "https://www.esa.int" + link
                next_pages.append(link)

        mission_name = response.xpath("//h1[@class='heading']/text()").get()

        text = response.css('div.mission-intro p::text').getall()
        # Extracting text inside the <a> tag
        tags = response.css('div.mission-intro a::text').get()

        complete_text = ""

        

        if (text is not None):
            if (tags is None and issubclass(type(text), str)):
                complete_text = text
            elif (tags is None and issubclass(type(text), list)):
                for phrase in text:
                    complete_text += phrase + " "
            else:
                if (issubclass(type(tags), str)):#Only one tag
                    complete_text = text[0] + tags + text[1]
                else:#more than one tags
                    for i in range(len(text)):
                        complete_text += text[i]  + " " + tags[i] + " "
            complete_text.strip()
    

        if (complete_text != ""):
            yield {'mission_name': mission_name,
                    'mission_description' : complete_text,
                    'mission_page' : response.url
            }
        for page in next_pages:
            yield response.follow(page, callback=self.parse)