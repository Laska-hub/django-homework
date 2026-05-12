from catalog.models import Product, Contact
from django.shortcuts import render, get_object_or_404


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


