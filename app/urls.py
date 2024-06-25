from django.contrib import admin
from django.urls import path, include
from .views import home, product_details, product_by_category

urlpatterns = [
    path('', home, name="home"),
    path('<int:id>/', product_by_category, name="product_by_category"),
    path("product/<int:id>", product_details, name='product_details'),
]