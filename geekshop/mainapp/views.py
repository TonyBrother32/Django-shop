from itertools import product
import json
from multiprocessing import context
from django.shortcuts import render
from django.utils import timezone
from .models import Product, ProductCategory

MENU_LINKS = [
    { 'url' : 'main', 'name' : 'домой'},
    { 'url' : 'products', 'name' : 'продукты'},
    { 'url' : 'contact', 'name' : 'контакты'},
]


def index (request):
    products = Product.objects.all()[:4]

    return render (request, 'mainapp/index.html', context={
        'title' : 'Главная',
        'menu_links' : MENU_LINKS,
        'datetime': timezone.now(),
        'products' : products,
    })

def contact (request):
    contacts = [
        { 
        'city' : 'Москва',
        'telephone' : '8498456531',
        'email' : 'moscow@design.ru',
        'delivery' : 'В пределах МКАД'
    }, { 
        'city' : 'Ленинград',
        'telephone' : '515645135',
        'email' : 'Lenin@design.ru',
        'delivery' : 'Не дальше 50км'
    }, { 
        'city' : 'Сталинград',
        'telephone' : '56561351321',
        'email' : 'Stalina@navas.net',
        'delivery' : 'Сами приедете'
    }]
    return render (request, 'mainapp/contact.html', context={
        'title' : 'Контакты',
        'contacts' : contacts,
        'datetime': timezone.now(),
        'menu_links' : MENU_LINKS,
    })

def products (request):
    categories = ProductCategory.objects.all()[:4]

    with open ( './geekshop/product.json', 'r', encoding='utf-8' ) as file:
        products = json.load(file)
       
    return render (request, 'mainapp/products.html', context={
        'title' : 'Продукты',
        'datetime': timezone.now(),
        'products' : products,
        'menu_links' : MENU_LINKS,
        'categories' : categories,
        })
    