from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """
    Creates new products
    """

    def handle(self, *args, **options):
        self.stdout.write("Create products")

        products_name = [
            "Desktop",
            "Laptop",
            "Smartphone",
        ]
        for products_name in products_name:
            product, created = Product.objects.get_or_create(name=products_name)
            self.stdout.write(f"Created product {product.name}")

        self.stdout.write(self.style.SUCCESS("Products created"))
