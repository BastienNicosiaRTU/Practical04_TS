import scrapy
from university_rankings.items import UniversityRankingItem

class RankingSpider(scrapy.Spider):
    name = 'ranking2'
    allowed_domains = ['shanghairanking.com']
    start_urls = ['https://www.shanghairanking.com/rankings/arwu/2023']

    def parse(self, response):
        for row in response.css('tr[data-v-ae1ab4a8]'):  #
            rank = row.css('div.ranking::text').get()
            university_name = row.css('span.univ-name::text').get()

            if rank and university_name:
                item = UniversityRankingItem()
                item['rank'] = rank.strip()
                item['university_name'] = university_name.strip()
                yield item


