from django.shortcuts import render
from catalog.models import Product, Contact


def home(request):
    products = Product.objects.order_by("-created_at")[:5]

    print(products)  # вывод в консоль (по заданию)

    return render(request, "home.html", {"products": products})


def contacts(request):
    contact = Contact.objects.first()

    return render(request, "contacts.html", {"contact": contact})
