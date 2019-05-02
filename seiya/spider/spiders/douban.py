# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250?start=%s' 
            %(i) for i in range(0, 251, 25)]

    def parse(self, response):
        item = MovieItem()
        for value in response.xpath('//ol[@class="grid_view"]/li'):
            item['name'] = value.css('span.title::text').extract_first()
            item['director'] = value.css(
                    'div.info p::text').extract_first().split()[1]
            item['country'] = value.css(
                    'div.info p::text').extract()[1].split('/')[1].strip() 
            item['tags'] = value.css(
                    'div.info p::text').extract()[1].split('/')[2].strip()
            item['grade'] = float(value.css(
                    'span.rating_num::text').extract_first())
            item['review_num'] = value.css(
                    'div.star span::text').extract()[1]
            yield item

