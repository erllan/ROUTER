from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from .models import Product, Category, Album, Brand
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'admin/index.html')


def allProduct(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'admin/Product.html', {'products': products, 'categories': categories})


def productForm(request):
    brands = Brand.objects.all()
    category = Category.objects.all()
    return render(request, 'admin/productForm.html', {'categories': category, 'brands': brands})


def all_category(request):
    category = Category.objects.all()

    return render(request, 'admin/category.html', {'categories': category})


def getOnbject(self, request, id_product):
    product = Product.objects.get(id=id_product)
    return render(request, 'admin/product.html', {'products': product})


def deleteBrand(request, id_object):
    brand = Brand.objects.get(id=id_object)
    brand.delete()
    return HttpResponse('удалено')


def category_set(request, id_object):
    category = Category.objects.get(id=id_object)
    products = category.product_set.all()
    return render(request, 'admin/category_set.html', {'products': products})


class BrandListCreate(View):
    """создать бренд POST,получить все бренды GET"""

    def get(self, request):
        brands = Brand.objects.all()
        return render(request, 'admin/brand.html', {'brands': brands})

    def post(self, request):
        brand_name = request.POST['brand']
        if len(brand_name) > 0:
            brand = Brand.objects.create(brand_name=brand_name)
            return HttpResponseRedirect(reverse('brand'))


class ProductDeleteCreate(View):
    """создание продукта [POST],удаление продукта[GET]"""

    def post(self, request):
        name = request.POST['title']
        desc = request.POST['description']
        photo = request.FILES['photo']
        price = request.POST['price']
        category = Category.objects.filter(pk__in=request.POST.getlist('category'))
        brand = Brand.objects.get(id=request.POST['brand'])
        size = request.POST['size']
        safety = request.POST['safety']
        interface = request.POST['interface']
        colors = request.POST['colors']
        if photo:
            myfile = request.FILES['photo']
            fs = FileSystemStorage(location='media/album')
            filename = fs.save(myfile.name, myfile)
            product = Product.objects.create(photo='/album/' + filename,
                                             title=name,
                                             description=desc,
                                             price=price,
                                             brand=brand,
                                             color=colors,
                                             size=size,
                                             safety=safety,
                                             interface=interface
                                             )
            product.category.add(*category)
            return HttpResponse('создано')

    def get(self, request, id_object):
        product = Product.objects.get(id=id_object)
        product.delete()
        return HttpResponseRedirect(reverse('products'))


class CreateDeleteCategory(View):
    """создание категории[POST],удаление категории [GET]"""

    def post(self, request):
        name = request.POST['category']
        if len(name) > 0:
            category = Category(category=name)
            category.save()
            return HttpResponseRedirect(reverse('category'))

    def get(self, request, id_object):
        category = Category.objects.get(id=id_object)
        category.delete()
        return HttpResponseRedirect(reverse('category'))


class DetailProductAndCreateAlbum(View):
    """Деталь продукта [GET],создать албьом [POST]"""
    def get(self, request, id_object):
        product = Product.objects.get(id=id_object)
        return render(request, 'admin/detailProduct.html', {'product': product})

    def post(self, request, id_object):
        if request.method == "POST":
            product = Product.objects.get(id=id_object)
            album = request.FILES['album']
            if album:
                myfile = album
                fs = FileSystemStorage(location='media/album')
                filename = fs.save(myfile.name, myfile)
                newAlbum = Album.objects.create(photo='/album/' + filename, to_product=product)
                return HttpResponse('создано')
