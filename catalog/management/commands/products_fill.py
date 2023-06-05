from django.core.management import BaseCommand
from catalog.models.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        food = Category.objects.get(category_name='Еда')
        clothes = Category.objects.get(category_name='Одежда')
        cars = Category.objects.get(category_name='Автомобили')
        drinks = Category.objects.get(category_name='Напитки')

        products_list = [
            {'product_name': 'Яблоко', 'description': 'Спелое, красное',
             'image': 'images/redapple.jpg', 'category': food, 'price': 400},
            {'product_name': 'Джинсы', 'description': 'Женские',
             'image': 'images/jeans.jpg', 'category': clothes, 'price': 300},
            {'product_name': 'БМВ', 'description': 'Серая машина',
             'image': 'images/bmw.jpg', 'category': cars, 'price': 1000},
            {'product_name': 'Молоко', 'description': 'Без лактозы',
             'image': 'images/milk.jpeg', 'category': drinks, 'price': 200},
        ]

        Product.objects.all().delete()

        created_products = []

        for product in products_list:
            created_products.append(
                Product(**product)
            )

        Product.objects.bulk_create(created_products)