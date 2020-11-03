from django.shortcuts import render, reverse
from .models import *
import json
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    saleProduct = Product.objects.all().order_by('-sale')
    sale = saleProduct.exclude(sale=0)
    category = Category.objects.all()
    return render(request, 'shop_router/index.html', {'categories': category, 'sales': sale})


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
                product = Product.objects.get(id=int(items['id']))
                Order.objects.create(product=product, from_customer=customer,
                                     order_quantities=items['count'])
            return HttpResponse('создано')
    return render(request, 'shop_router/form.html')


def addCountOrder(request, id_object):
    if request.COOKIES.get('Order'):
        response = HttpResponse(json.dumps({"status": 200}), content_type="application/json")
        cook = request.COOKIES.get('Order')
        des = cook.replace("'", '"')
        data = json.loads(des)
        for item in data['data']:
            if id_object == item['id']:
                item['count'] += 1
        response.set_cookie("Order", data, max_age=3600)
        return response


def minusCountOrder(request, id_object):
    if request.COOKIES.get('Order'):
        response = HttpResponse(json.dumps({"status": 200}), content_type="application/json")
        cook = request.COOKIES.get('Order')
        des = cook.replace("'", '"')
        data = json.loads(des)
        for item in data['data']:
            if id_object == item['id']:
                if item['count'] > 0:
                    item['count'] -= 1
        response.set_cookie("Order", data, max_age=3600)
        return response


def order(request):
    order_data = request.COOKIES.get('Order')
    if order_data:
        des = order_data.replace("'", '"')
        order_id = json.loads(des)
        ids = []
        productCouunts = {}
        for item in order_id['data']:
            productCouunts[item['id']] = item['count']
            ids.append(int(item['id']))
        order_product = Product.objects.filter(id__in=ids)
        total = 0
        allSale = 0
        for object in order_product:
            total += object.price
            allSale += (object.price-object.get_sale())

        return render(request, 'shop_router/order.html',
                      {'product': order_product, 'counts': productCouunts, 'total': total-allSale, 'allSale': allSale})
    return render(request, 'shop_router/basket.html')


def addProductToBascet(request, id_object, count=1):
    if request.COOKIES.get("Order"):
        response = HttpResponse("ваш заказ")
        orderCookie = request.COOKIES.get("Order")
        des = orderCookie.replace("'", '"')
        dataCookie = json.loads(des)
        dataCookie["data"].append({"id": id_object, "count": count})
        response.set_cookie("Order", dataCookie, max_age=3600)

    else:
        data = json.dumps({"data": [{"id": id_object, "count": count}]})
        response = HttpResponse("ваш заказ добавлен в карзину")
        response.set_cookie("Order", data, max_age=3600)
    return response


def product(request, id_obj):
    prod = Product.objects.get(id=id_obj)
    recoment = prod.brand.product_set.all()
    return render(request, 'shop_router/product.html', {'product': prod, 'recoment': recoment})


def routers(request):
    return render(request, 'shop_router/routers.html')


def about(request):
    return render(request, 'shop_router/about.html')
