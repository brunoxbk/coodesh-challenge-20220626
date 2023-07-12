# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from products.models import Product
from asgiref.sync import sync_to_async


def clean_barcode(param):
    return param.strip().replace('Barcode:', '').strip()


class CrawlingPipeline(object):

    @sync_to_async
    def process_item(self, item, spider):
        item['barcode'] = clean_barcode(item['barcode'])

        product, created = Product.objects.get_or_create(
            code=item['code'],
            defaults=item,
        )

        return product
