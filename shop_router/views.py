from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    return render(request, 'shop_router/index.html', {'products': products})


def basket(request):
    return render(request, 'shop_router/basket.html')


def form(request):
    return render(request, 'shop_router/form.html')


def order(request):
    a = request.COOKIES.get('Order')
    if a:
        order_product = Product.objects.filter(id__in=int(a))
        return render(request, 'shop_router/order.html', {'product': order_product})
    return render(request, 'shop_router/basket.html')


def addProductToBascet(request, id_object):
    if request.COOKIES.get('Order'):
        response = request.COOKIES['Order']
    else:
        response = HttpResponse('ваш заказ добавлен в карзину')
        response.set_cookie('Order', id_object, max_age=15)
    return response


def product(request, id_obj):
    prod = Product.objects.get(id=id_obj)
    return render(request, 'shop_router/product.html', {'product': prod})


def routers(request):
    return render(request, 'shop_router/routers.html')


def about(request):
    return render(request, 'shop_router/about.html')
