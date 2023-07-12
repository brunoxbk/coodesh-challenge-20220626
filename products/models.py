from django.db import models


class Product(models.Model):
    """
        "code": 3661112502850,
        "barcode": "3661112502850(EAN / EAN-13)",
        "status": "imported",
        "imported_t": "2020-02-07T16:00:00Z",
        "url": "https://world.openfoodfacts.org/product/3661112502850",
        "product_name": "Jambon de Paris cuit à l'étouffée",
        "quantity": "240 g",
        "categories": "Meats, Prepared meats, Hams, White hams",
        "packaging": "Film en plastique, Film en plastique",
        "brands": "Tradilège, Marque Repère",
        "image_url": "https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg"
    """

    class StatusChoices(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        IMPORTED = 'IMPORTED', 'Imported'

    code = models.BigIntegerField("Code", unique=True, blank=False, null=False)
    barcode = models.CharField(
        'Barcode', blank=False, null=False, max_length=200)
    product_name = models.CharField(
        'Product Name', blank=False, null=False, max_length=200)
    url = models.CharField('Url', blank=False, null=False, max_length=200)
    quantity = models.CharField(
        'Barcode', blank=False, null=False, max_length=50)
    categories = models.CharField(
        'Categories', blank=False, null=False, max_length=500)
    packaging = models.CharField(
        'Packaging', blank=False, null=False, max_length=200)
    brands = models.CharField('Brands', blank=False,
                              null=False, max_length=200)
    image_url = models.CharField(
        'Image', blank=False, null=False, max_length=250)

    imported_t = models.DateTimeField("Date Imported", auto_now_add=True)
    status = models.CharField(
        'Status', default=StatusChoices.DRAFT, blank=False,
        null=False, choices=StatusChoices.choices, max_length=10)

    class Meta:
        ordering = ['-pk']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
