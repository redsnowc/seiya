# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import RestaurantItem


class RestaurantSpider(scrapy.Spider):
    name = 'restaurant'
    start_urls = ['http://www.dianping.com/nanjing/ch10/p%s/' 
            for i in range(1,51)]

    def parse(self, response):
        item = RestaurantItem()
        for value in response.xpath(
            '//div[@class="shop-list J_shop-list shop-all-list"]/ul/li'):
            item['name'] = value.css('h4::text').extract_first()
            item['review_num'] = value.css('')
