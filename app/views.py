from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    print(products)
    context = {
        "products": products,
        'categories':categories
    }
    return render(request, "index.html", context)

def product_by_category(request, id):
    products = Product.objects.filter(category=id).order_by('-price')
    categories = Category.objects.all()
    print(products)
    context = {
        "products": products,
        'categories':categories
    }
    return render(request, "index.html", context)


def product_details(request, id):
    products = Product.objects.get(id=id)
    context = {
        "products": products
    }
    return render(request, "product-detail.html", context)