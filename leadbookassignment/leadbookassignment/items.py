# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeadbookassignmentItem(scrapy.Item):
    company_name = scrapy.Field()
    source_url = scrapy.Field()
 
