from django.shortcuts import render


def index(request):
    return render(request, 'shop_router/index.html')


def basket(requser):
    return render(requser, 'shop_router/basket.html')


def form(request):
    return render(request, 'shop_router/form.html')


def order(request):
    return render(request, 'shop_router/order.html')


def product(request):
    return render(request, 'shop_router/product.html')


def routers(request):
    return render(request, 'shop_router/routers.html')


def about(request):
    return render(request, 'shop_router/about.html')
