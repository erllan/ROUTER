from django.shortcuts import render, reverse
from .models import *
import json
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    category = Category.objects.all()
    return render(request, 'shop_router/index.html', {'categories': category})


def basket(request):
    return render(request, 'shop_router/basket.html')


def form(request):
    testOrder = request.COOKIES.get('Order')
    if testOrder:
        if request.method == 'POST':
            full_name = request.POST['full_name']
            phone = request.POST['phone']
            email = request.POST['email']
            city = request.POST['city']
            comment = request.POST['comment']
            customer = Customer.objects.create(full_name=full_name, phone=phone, Email=email, delivery_city=city,
                                              Comment=comment)
            des = testOrder.replace("'", '"')
            data = json.loads(des)
            for items in data['data']:
                Order.objects.create(product_id=items['id'], from_customer_id=customer.id,
                                     order_quantities=items['count'])
            return HttpResponse('создано')
    return render(request, 'shop_router/form.html')


def addCountOrder(request, id_object):
    if request.COOKIES.get('Order'):
        response = HttpResponse("тест куки")
        cook = request.COOKIES.get('Order')
        des = cook.replace("'", '"')
        data = json.loads(des)
        for item in data['data']:
            if id_object == item['id']:
                item['count'] += 1
        response.set_cookie("Order", data, max_age=100)
        return response


def order(request):
    order_data = request.COOKIES.get('Order')
    if order_data:
        des = order_data.replace("'", '"')
        order_id = json.loads(des)
        id = []
        for item in order_id['data']:
            id.append(int(item['id']))
        order_product = Product.objects.filter(id__in=id)
        return render(request, 'shop_router/order.html', {'product': order_product})
    return render(request, 'shop_router/basket.html')


def addProductToBascet(request, id_object, count=1):
    if request.COOKIES.get("Order"):
        response = HttpResponse("ваш заказ")
        orderCookie = request.COOKIES.get("Order")
        des = orderCookie.replace("'", '"')
        dataCookie = json.loads(des)
        dataCookie["data"].append({"id": id_object, "count": count})
        response.set_cookie("Order", dataCookie, max_age=100)

    else:
        data = json.dumps({"data": [{"id": 1, "count": count}]})
        response = HttpResponse("ваш заказ добавлен в карзину")
        response.set_cookie("Order", data, max_age=100)
    return response


def product(request, id_obj):
    prod = Product.objects.get(id=id_obj)
    return render(request, 'shop_router/product.html', {'product': prod})


def routers(request):
    return render(request, 'shop_router/routers.html')


def about(request):
    return render(request, 'shop_router/about.html')
