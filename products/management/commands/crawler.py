from django.core.management.base import BaseCommand, CommandError
import requests
import requests
from bs4 import BeautifulSoup as BSoup
from products.models import Product


class Command(BaseCommand):
    help = "start to scrapy"
    base_url = "https://world.openfoodfacts.org"

    def handle(self, *args, **options):

        try:

            request = requests.get(self.base_url)
            print(request)
            soup = BSoup(request.text, "html.parser")

            title = soup.find("title")
            print(title)

            # ok
            # search_results = soup.find('div', id="search_results")
            # print(search_results)

            products = soup.find('ul', class_="products")
            # print(products)

            products_itens = products.find_all('li')

            for item in products_itens[:10]:
                # print(item)
                item_href = item.find("a").attrs['href']
                product_name = item.find("span").text

                self.stdout.write(
                    self.style.WARNING('crawler %s' % product_name)
                )

                request_item = requests.get(f"{self.base_url}{item_href}")

                soup_item = BSoup(request_item.text, "html.parser")

                section = soup_item.find("section", id="product")

                item = dict()

                item['code'] = int(
                    section.find("span", id="barcode").text)
                barcode_paragraph = section.find(
                    "p", id="barcode_paragraph").text
                item['code'] = section.find("span", id="barcode").text
                item['barcode'] = barcode_paragraph.strip().replace(
                    'Barcode:', '').strip()
                item['status'] = Product.StatusChoices.DRAFT
                item['imported_t'] = ''
                item['url'] = f"{self.base_url}{item_href}"
                item['product_name'] = product_name
                item['quantity'] = section.find(
                    "span", id="field_quantity_value").text
                item['categories'] = section.find(
                    "span", id="field_categories_value").text
                item['packaging'] = section.find(
                    "span", id="field_packaging_value").text
                item['brands'] = section.find(
                    "span", id="field_brands_value").text
                item['image_url'] = section.find(
                    "img", id="og_image").attrs['src']

                p, created = Product.objects.get_or_create(
                    code=item['code'],
                    defaults=item,
                )

                print('# --------------------------------------------- #')

        except Exception as e:
            raise CommandError(str(e))

        self.stdout.write(
            self.style.SUCCESS('Successfully')
        )
