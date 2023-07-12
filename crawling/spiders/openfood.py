import scrapy
from crawling.items import ProductItem
from bs4 import BeautifulSoup as BSoup


class OpenFoodSpider(scrapy.Spider):

    name = 'openfood'
    allowed_domains = ['world.openfoodfacts.org']
    start_urls = ['https://world.openfoodfacts.org',]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('aqui')
        print(response)
        soup = BSoup(response.text, "html.parser")

        products = soup.find('ul', class_="products")

        products_itens = products.find_all('li')

        for item in products_itens[:10]:

            item_href = item.find("a").attrs['href']
            product_name = item.find("span").text

            link = f"https://world.openfoodfacts.org{item_href}"

            yield scrapy.Request(
                link, callback=self.parse_item,
                meta={'product_name': product_name, 'item_href': item_href})

    def parse_item(self, response):
        item_href = response.meta.get('item_href')
        product_name = response.meta.get('product_name')
        item = ProductItem()

        soup_item = BSoup(response.text, "html.parser")

        section = soup_item.find("section", id="product")

        item['code'] = int(
            section.find("span", id="barcode").text)

        item['code'] = section.find("span", id="barcode").text
        barcode_paragraph = section.find(
            "p", id="barcode_paragraph").text
        item['barcode'] = barcode_paragraph
        item['imported_t'] = ''
        item['url'] = f"https://world.openfoodfacts.org{item_href}"
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

        return item
