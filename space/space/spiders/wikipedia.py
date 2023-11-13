import scrapy
import time

base_site_url = "https://en.wikipedia.org/"

class Test_spider(scrapy.Spider):

    name = "wikipedia"

    start_urls = ["https://en.wikipedia.org/wiki/Timeline_of_space_exploration"]

    row_processed = 0


    def parse(self, response):    # Funcion called every crawled web page. The response parameter will contain the web site response.
        next_pages = []
        for row in response.css('tbody tr'):
            
            self.row_processed += 1 

            if self.row_processed < 37:#Exclusion of the first tables which is not as usefull as the others to use
                continue

            date = row.css('td:nth-child(1)::text').get()
            if date == "\n":
                date = row.css('td:nth-child(1) span::text').get()

            
            # Extract text within <td> tags, including text within <a> tags
            event_text_elements = row.css('td:nth-child(2) *::text').getall()
            event_text = ' '.join(event_text_elements)

            country = row.css('td:nth-child(3)::text').get()
            
            # Extract href attribute from the <a> tag in the researcher/Mission name column
            mission_href = row.css('td:nth-child(4) a::attr(href)').get()
            mission_text = row.css('td:nth-child(4) a::text').get()

            references = row.css('td:nth-child(5)::text').get()
            if mission_href is not None:
                new_page = base_site_url + mission_href
                next_pages.append(new_page)

            yield {
                'Date': date.strip() if date else None,
                'Event': event_text.strip() if event_text else None,
                'Country': country.strip() if country else None,
                'Mission name': {'text': mission_text.strip() if mission_text else None, 'href': mission_href.strip() if mission_href else None},
                'References': references.strip() if references else None,
            }

            







