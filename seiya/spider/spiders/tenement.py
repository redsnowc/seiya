# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import TenementItem


class TenementSpider(scrapy.Spider):
    name = 'tenement'
    start_urls = [
            'https://nj.lianjia.com/zufang/ab200301001000pg%srt200600000001/' %(i) for i in range(1, 51)
            ]

    def parse(self, response):
        item = TenementItem()
        for value in response.xpath('//div[@class="content__list--item"]'):
            item['title'] = value.css(
                'p.content__list--item--title a::text').extract_first().strip().replace('，', ' ')
            item['region'] = value.css(
                'p.content__list--item--des a::text').extract_first()
            item['area'] = value.css(
                'p.content__list--item--des::text').re_first(
                    '\s.*\s(\d+)㎡')
            item['unit'] = value.css(
                'p.content__list--item--des::text').extract()[5].strip()
            item['rent'] = value.css(
                'span.content__list--item-price em::text').extract_first()
            yield item

