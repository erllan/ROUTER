from django.shortcuts import render, reverse
from .models import *
import json
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import ProductSerializers
from rest_framework.views import APIView


class Search(APIView):
    def get(self, request, format=None):
        search = request.GET['title']
        result = Product.objects.filter(title__icontains=search)
        serializer = ProductSerializers(result, many=True)
        return HttpResponse(serializer.data)


def allCatalog():
    catalog = Catalog.objects.all()
    return catalog


def index(request):
    catalog = allCatalog()
    saleProduct = Product.objects.all().order_by('-sale')
    sale = saleProduct.exclude(sale=0)
    hits = saleProduct.filter(hit=True)
    return render(request, 'shop_router/index.html', {'sales': sale[:3], 'catalogs': catalog, 'hits': hits})


def category_set(request, id_object):
    catalog = allCatalog()
    category = Category.objects.get(id=id_object)
    return render(request, 'shop_router/category.html', {'category': category, 'catalogs': catalog})


def basket(request):
    catalog = allCatalog()
    return render(request, 'shop_router/basket.html', {'catalogs': catalog})


def form(request):
    catalog = allCatalog()
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
    return render(request, 'shop_router/form.html', {'catalogs': catalog})


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
    catalog = allCatalog()
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
            allSale += (object.price - object.get_sale())

        return render(request, 'shop_router/order.html',
                      {'product': order_product, 'counts': productCouunts, 'total': total - allSale,
                       'allSale': allSale, 'catalogs': catalog})
    return render(request, 'shop_router/basket.html', {'catalogs': catalog})


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
    catalog = allCatalog()
    prod = Product.objects.get(id=id_obj)
    recoment = prod.brand.product_set.all()
    return render(request, 'shop_router/product.html', {'product': prod, 'recoment': recoment, 'catalogs': catalog})


def routers(request, id_object):
    catalog = allCatalog()
    catalog_set = Catalog.objects.get(id=id_object)
    return render(request, 'shop_router/routers.html', {'catalogs': catalog, 'catalog_set': catalog_set})


def about(request):
    catalog = allCatalog()
    return render(request, 'shop_router/about.html', {'catalogs': catalog})
