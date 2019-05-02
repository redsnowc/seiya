# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SeiyaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    title = scrapy.Field()
    city = scrapy.Field()
    salary_lower = scrapy.Field()
    salary_upper = scrapy.Field()
    experience_lower = scrapy.Field()
    experience_upper = scrapy.Field()
    education = scrapy.Field()
    tags = scrapy.Field()
    company = scrapy.Field()

class TenementItem(scrapy.Item):
    title = scrapy.Field()
    area = scrapy.Field()
    unit = scrapy.Field()
    region = scrapy.Field()
    rent = scrapy.Field()

class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    review_num = scrapy.Field()
    grade = scrapy.Field()
    per_capita = scrapy.Field()
    kind = scrapy.Field()
    taste = scrapy.Field()
    env = scrapy.Field()
    service = scrapy.Field()
    area = scrapy.Field()

class MovieItem(scrapy.Item):
    name = scrapy.Field()
    director = scrapy.Field()
    grade = scrapy.Field()
    review_num =scrapy.Field()
    tags = scrapy.Field()
    country = scrapy.Field()

