from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    category = Category.objects.all()
    return render(request, 'shop_router/index.html', {'categories': category})


def basket(request):
    return render(request, 'shop_router/basket.html')


def form(request):
    return render(request, 'shop_router/form.html')


def order(request):
    a = request.COOKIES.get('Order')
    if a:
        b = a.split(',')
        result = [int(item) for item in b]
        print(result)
        order_product = Product.objects.filter(id__in=result)
        return render(request, 'shop_router/order.html', {'product': order_product})
    return render(request, 'shop_router/basket.html')


def addProductToBascet(request, id_object):
    if request.COOKIES.get('Order'):
        response = HttpResponse('ваш заказ')
        value = request.COOKIES.get('Order')
        response.set_cookie('Order', value + ',' + str(id_object), max_age=60)

    else:
        response = HttpResponse('ваш заказ добавлен в карзину')
        response.set_cookie('Order', id_object, max_age=60)
    return response


def product(request, id_obj):
    prod = Product.objects.get(id=id_obj)
    return render(request, 'shop_router/product.html', {'product': prod})


def routers(request):
    return render(request, 'shop_router/routers.html')


def about(request):
    return render(request, 'shop_router/about.html')
