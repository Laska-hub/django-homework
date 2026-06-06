from django.shortcuts import render, get_object_or_404
from django.core.cache import cache

from catalog.models import Product, Contact
from catalog.services import get_products_by_category


def home(request):
    products = Product.objects.all()

    return render(request, "home.html", {
        "products": products
    })


def contacts(request):
    contact = Contact.objects.first()

    return render(request, "contacts.html", {"contact": contact})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "product_detail.html", {
        "product": product
    })


def category_products(request, category_id):
    key = f"category_{category_id}"

    products = cache.get(key)

    if products is None:
        products = get_products_by_category(category_id)
        cache.set(key, products, 60 * 15)

    return render(request, "catalog/category_products.html", {
        "products": products,
        "category_id": category_id
    })
