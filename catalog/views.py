from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contact, Category
from catalog.services import get_products_by_category


def home(request):
    products = Product.objects.all()

    return render(
        request,
        "home.html",
        {
            "products": products,
        },
    )


def contacts(request):
    contact = Contact.objects.first()

    return render(
        request,
        "contacts.html",
        {
            "contact": contact,
        },
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        "product_detail.html",
        {
            "product": product,
        },
    )


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    products = get_products_by_category(category_id)

    return render(
        request,
        "catalog/category_products.html",
        {
            "products": products,
            "category": category,
        },
    )
