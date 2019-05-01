# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from seiya.db.job import session, Job
from seiya.db.tenement import Tenement
from seiya.spider.items import JobItem, TenementItem


class SeiyaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, JobItem):
            self._process_job_item(item)
        elif isinstance(item, TenementItem):
            self._process_tenement_item(item)
        return item

    def _process_job_item(self, item):
        item['salary_lower'] = int(item['salary_lower'])
        item['salary_upper'] = int(item['salary_upper'])
        item['experience_lower'] = int(item['experience_lower'])
        item['experience_upper'] = int(item['experience_upper'])

        session.add(Job(**item))

    def _process_tenement_item(self, item):
        item['title'] = item['title'].split()[0]
        item['rent'] = int(item['rent'])
        item['area'] = int(item['area'])

        session.add(Tenement(**item))

    def close_spider(self, spider):
        session.commit()
        session.close()

