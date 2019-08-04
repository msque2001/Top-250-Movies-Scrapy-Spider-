import scrapy

class ImdbScraper(scrapy.Spider):
    name = "twoFifty"

    start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250']

    def parse(self, response):
 
        for row in response.css('tbody>tr'):
            title = row.css('td.titleColumn>a::text').get()
            year = row.css('td.titleColumn>span.secondaryInfo::text').get()[1:5]
            rating = row.css('td.imdbRating>strong::text').get()

            yield { 'title':title, 'year':year, 'rating':rating} 
        

