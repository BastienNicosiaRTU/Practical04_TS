# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UniversityRankingItem(scrapy.Item):
    rank = scrapy.Field()
    university_name = scrapy.Field()

