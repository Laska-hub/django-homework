from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Load test data into database"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Создаем категории...")

        phones = Category.objects.create(
            name="Телефоны",
            description="Смартфоны"
        )

        fruits = Category.objects.create(
            name="Фрукты",
            description="Фруктовая категория"
        )

        self.stdout.write("Создаем продукты...")

        Product.objects.create(
            name="iPhone",
            description="Apple phone",
            price=1000,
            category=phones
        )

        Product.objects.create(
            name="Samsung",
            description="Android phone",
            price=800,
            category=phones
        )

        Product.objects.create(
            name="Мандарин",
            description="Сладкий фрукт",
            price=2,
            category=fruits
        )

        self.stdout.write(self.style.SUCCESS("Готово! Данные загружены"))
