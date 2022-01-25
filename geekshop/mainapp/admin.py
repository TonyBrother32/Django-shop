from atexit import register
from itertools import product
from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)