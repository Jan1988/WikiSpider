# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib


class WikispiderPipeline(object):

    def process_item(self, item, spider):

        filename = item['url'][7:].replace('/', '_')

        print(filename)

        with open('%s.html' % filename, 'w+b') as f:
            f.write(item['html'])

        return item
