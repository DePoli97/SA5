import time
import scrapy
import pyterrier as pt
if not pt.started():
  pt.init()
import pandas as pd

class Test_spider(scrapy.Spider):

    name = "nasa"

    start_urls = [
        "https://www.nasa.gov/missions/"
                  ]

    def parse(self, response):    # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []

        i = 0
        for mission in response.xpath("//div[@class='hds-content-item hds-content-item-card hds-search-result mission-terms-result-container']"):
            yield {
                    'missionNumber': i,
                    'mission_name': mission.xpath(".//h4[@class='hds-content-item-heading, color-carbon-black, heading-20, mission-terms-result-title']/text()"),
                    'text': mission.xpath(".//div[@class='hds-content-item-excerpt, mission-terms-result-excerpt']/text()")
            }
            i = i + 1



        docs_df = pd.DataFrame[[
            'mission_name',
            'text'
        ]]




