from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение",
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.country
