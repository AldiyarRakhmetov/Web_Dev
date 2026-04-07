from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product

# Create your views here.

def products(request):
    products_ = Product.objects.all()

    products_json = []

    for p in products_:
        products_json.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id
        })

    return JsonResponse(products_json, safe=False)


def product(request, id):
    p = Product.objects.get(id=id)
    
    p_json = {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'count': p.count,
        'is_active': p.is_active,
        'category_id': p.category.id
    }
    
    return JsonResponse(p_json)


def categories(request):
    categories_ = Category.objects.all()

    categories_json = []

    for c in categories_:
        categories_json.append({
            'id': c.id,
            'name': c.name
        })
    
    return JsonResponse(categories_json, safe=False)


def category(request, id):
    c = Category.objects.get(id=id)
    
    c_json = {
        'id': c.id,
        'name': c.name
    }

    return JsonResponse(c_json)


def products_of_category(request, id):
    products = Product.objects.filter(category_id=id)

    products_json = []

    for p in products:
        products_json.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id
        })

    return JsonResponse(products_json, safe=False)

def active_products(request, activity):
    if activity == "true":
        products = Product.objects.filter(is_active=True)
    else:
        products = Product.objects.filter(is_active=False)

    products_json = []

    for p in products:
        products_json.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
            'category_id': p.category.id
        })

    return JsonResponse(products_json, safe=False)