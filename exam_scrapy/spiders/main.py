from numpy import arange
import scrapy


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['www.examtopics.com']
    start_urls = ['https://www.examtopics.com/discussions/comptia/1/']


    def parse(self, response):
        for i in response.css('div.row.discussion-row'):
            if 'PT0-001 ' in i.css('a.discussion-link::text').get().strip():
                yield {'page' : 'page number : `'+response.css('span.discussion-list-page-indicator strong::text').get() , 'name' : i.css('a.discussion-link::text').get().strip() ,'link' : f"https://www.examtopics.com/{i.css('a.discussion-link::attr(href)').get()}"}
        if response.css('span.discussion-list-page-indicator strong::text').get() != 279:
            yield scrapy.FormRequest(f'https://www.examtopics.com{response.css("a.btn.btn-sm::attr(href)").getall()[1]}' ,dont_filter=True, callback=self.parse)




                                            