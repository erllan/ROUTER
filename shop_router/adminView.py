from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from .models import Product, Category, Album, Brand, Customer, Catalog
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

"""Каталог и категории"""


def catalog(request):
    c = Catalog.objects.all()
    return render(request, 'admin/catalog.html', {'catalogs': c})


def createCatalog(request):
    if request.method == 'POST':
        if len(request.POST['title']) > 0:
            create = Catalog(title=request.POST['title'])
            create.save()
            return HttpResponseRedirect(reverse('catalogs', ))
    catalogs = Catalog.objects.all()
    return render(request, 'admin/catalogs.html', {'catalogs': catalogs})


def getCatalog(request, id_object):
    catalog = Catalog.objects.get(id=id_object)
    if request.method == "POST":
        Category.objects.create(category=request.POST['category'], catalog=catalog)
    return render(request, 'admin/detailCatalog.html', {'catalog': catalog})


def detailCategory(request, id_object):
    category = Category.objects.get(id=id_object)
    return render(request, 'admin/category.html', {'category': category})


def deleteCategory(request, id_object):
    obj = Category.objects.get(id=id_object)
    obj.delete()
    return HttpResponse('удалено')


def deleteCatalog(request, id_object):
    obj = Catalog.objects.get(id=id_object)
    obj.delete()
    return HttpResponseRedirect(reverse('catalogs', ))


"""."""


def login_admin(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('admin.index'))
        else:
            error = 'неправильный логин или пароль'
    return render(request, 'registration/login.html', {'error': error})


def index(request):
    if request.user.is_authenticated:
        return render(request, 'admin/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))


def sale(request, id_object):
    if request.method == 'POST':
        prod = Product.objects.get(id=id_object)
        prod.sale = int(request.POST['sale'])
        prod.save()
        return HttpResponse('акция')


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def allProduct(request):
    products = Product.objects.all().order_by('-date')
    return render(request, 'admin/Product.html', {'products': products})


def productForm(request, id_objects):
    brands = Brand.objects.all()
    catalog = Catalog.objects.get(id=id_objects)
    category = catalog.category_set.all()
    return render(request, 'admin/productForm.html', {'categories': category, 'brands': brands})


def getOnbject(self, request, id_product):
    product = Product.objects.get(id=id_product)
    return render(request, 'admin/product.html', {'products': product})


def deleteBrand(request, id_object):
    brand = Brand.objects.get(id=id_object)
    brand.delete()
    return HttpResponse('удалено')


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
            product = Product.objects.create(
                title=name,
                description=desc,
                price=price,
                brand=brand,
                color=colors,
                size=size,
                safety=safety,
                interface=interface
            )
            Album.objects.create(photo='/album/' + filename, to_product=product)
            product.category.add(*category)
            return HttpResponse('создано')

    def get(self, request, id_object):
        product = Product.objects.get(id=id_object)
        product.delete()
        return HttpResponseRedirect(reverse('products'))


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


def order(request, id_object):
    customer = Customer.objects.get(id=id_object)
    return render(request, 'admin/order.html', {'customer': customer})


def customer(request):
    all_customer = Customer.objects.all().order_by('-order_date')
    return render(request, 'admin/customers.html', {'customers': all_customer})


def deleteCustomer(request, id_object):
    obj = Customer.objects.get(id=id_object)
    obj.delete()
    return HttpResponseRedirect(reverse('customer'))


def hit(request, id_object):
    obj = Product.objects.get(id=id_object)
    obj.hit = True
    obj.save()


def hits(request):
    objects = Product.objects.all()
    objHit = Product.objects.filter(hit=True)
    return render(request, 'admin/hits.html', {'products': objects, 'hits': objHit})
