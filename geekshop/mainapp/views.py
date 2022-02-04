import random
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, ProductCategory

MENU_LINKS = [
    { 'url' : 'main', 'active': ['main'],'name' : 'домой'},
    { 'url' : 'mainapp:products', 'active': ['products:products', 'products:category'], 'name' : 'продукты'},
    { 'url' : 'contact', 'active': ['contact'],'name' : 'контакты'},
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

def get_hot_product(queryset):
    return random.choice(queryset)

def product (request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = ProductCategory.objects.all()
    
    return render (request, 'mainapp/product.html', 
    context={
        'title' : 'Продукты',
        'datetime': timezone.now(),
        'product' : product,
        'menu_links' : MENU_LINKS,
        'categories' : categories,
        })
    

def products (request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    hot_product = get_hot_product(products)

    return render (request, 'mainapp/products.html', 
    context={
        'title' : 'Продукты',
        'hot_product' : hot_product,
        'products' : products.exclude(pk=hot_product.pk)[:4],
        'datetime': timezone.now(),
        'menu_links' : MENU_LINKS,
        'categories' : categories,
        })

def category (request, category_id):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)

    return render (request, 'mainapp/products.html', 
    context={
        'title' : 'Продукты',
        'datetime': timezone.now(),
        'products' : products.exclude(pk=hot_product.pk)[:4],
        'hot_product' : get_hot_product(products),
        'menu_links' : MENU_LINKS,
        'categories' : categories,
        })
    