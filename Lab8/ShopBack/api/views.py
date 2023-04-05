from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def getProductList(request):
    data = Product.objects.all()
    list = [
        {
            'id': i.id,
            'name': i.name,
            'price': i.price,
            'description': i.description,
            'count': i.count,
            'is_active': i.is_active
        } for i in data
    ]
    return JsonResponse(data=list, safe=False)

def getProduct(request, *args, **kwargs):
    product_id = int(kwargs['id'])
    data = Product.objects.get(id=product_id)
    data = [{
            'id': data.id,
            'name': data.name,
            'price': data.price,
            'description': data.description,
            'count': data.count,
            'is_active': data.is_active
            }]
    return JsonResponse(data=data, safe=False)


def getCategories(request):
    data = Category.objects.all()
    d = [
        {
            'id': i.id,
            'name': i.name
        } for i in data
    ]
    return JsonResponse(d, safe=False)


def getCategory(request, **kwargs):
    category_id = int(kwargs['id'])
    data = Category.objects.get(id=category_id)
    list = [
        {
          'id': data.id,
          'name': data.name
        }
    ]
    return JsonResponse(list, safe=False)


def getByCategory(request, **kwargs):
    products = Product.objects.filter(category__id=int(kwargs['id']))
    data = [{
        'category_id': i.category.id,
        'category_name': i.category.name,
        'product_id': i.id,
        'product_name': i.name,
        'product_price': i.price,
        'product_description': i.description,
        'product_count': i.count,
        'product_is_active': i.is_active
    } for i in products]
    return JsonResponse(data=data, safe=False)