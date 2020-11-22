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


"""User"""


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
        all_customer = Customer.objects.all().order_by('-order_date')
        return render(request, 'admin/index.html', {'customers': all_customer})
    else:
        return HttpResponseRedirect(reverse('login'))


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


"""Brand"""


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


"""View Product"""


# данные формы для создание продукта
def productForm(request, id_objects):
    brands = Brand.objects.all()
    category_set = Category.objects.get(id=id_objects)
    category = category_set.set_category.all()
    return render(request, 'admin/productForm.html', {'categories': category, 'brands': brands})


def allProduct(request):
    products = Product.objects.all().order_by('-date')
    return render(request, 'admin/product.html', {'products': products})


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


def hit(request, id_object):
    obj = Product.objects.get(id=id_object)
    obj.hit = True
    obj.save()
    return HttpResponseRedirect('/admin/hit/')


def deleteHit(request, id_object):
    obj = Product.objects.get(id=id_object)
    obj.hit = False
    obj.save()
    return HttpResponseRedirect('/admin/hit/')


def hits(request):
    objects = Product.objects.all()
    objHit = Product.objects.filter(hit=True)
    return render(request, 'admin/hits.html', {'products': objects, 'hits': objHit})


def sale(request, id_object):
    if request.method == 'POST':
        prod = Product.objects.get(id=id_object)
        if len(request.POST['sale']) > 0 and len(request.POST['price']) > 0:
            prod.sale = int(request.POST['sale'])
            prod.price = int(request.POST['price'])
            prod.save()
        return HttpResponseRedirect(reverse('detailProduct', args=(prod.id,)))


class DetailProductAndCreateAlbum(View):
    """Деталь продукта [GET],создать албьом [POST]"""

    def get(self, request, id_object):
        brands = Brand.objects.all()
        product = Product.objects.get(id=id_object)
        category = product.category.all()
        categories = False
        if category:
            c = Category.objects.get(id=category[0].children_category.id)
            categories = c.set_category.all()

        return render(request, 'admin/detailProduct.html',
                      {'product': product, 'brands': brands, 'categories': categories})

    def post(self, request, id_object):
        product = Product.objects.get(id=id_object)
        product.title = request.POST['title']
        product.description = request.POST['description']
        category = Category.objects.filter(pk__in=request.POST.getlist('category'))
        product.brand = Brand.objects.get(id=request.POST['brand'])
        product.size = request.POST['size']
        product.safety = request.POST['safety']
        product.interface = request.POST['interface']
        product.colors = request.POST['colors']
        product.save()
        test = product.category.all()
        product.category.remove(*test)
        product.category.add(*category)
        return HttpResponseRedirect(reverse('detailProduct', args=(product.id,)))


class AddDeleteAlbum(View):

    def post(self, request, id_object):
        product = Product.objects.get(id=id_object)
        if request.FILES['album']:
            myfile = request.FILES['album']
            fs = FileSystemStorage(location='media/album')
            filename = fs.save(myfile.name, myfile)
            Album.objects.create(photo='/album/' + filename, to_product=product)
            return HttpResponseRedirect(reverse('detailProduct', args=(product.id,)))

    def get(self, request, id_object):
        album = Album.objects.get(id=id_object)
        album.delete()
        return HttpResponseRedirect(reverse('detailProduct', args=(album.to_product.id,)))


"""View Order and Customer"""


def order(request, id_object):
    customer = Customer.objects.get(id=id_object)
    total = 0
    allSale = 0
    order = customer.order_set.all()
    for object in order:
        total += object.product.price
        allSale += (object.product.price - object.product.get_sale())
    return render(request, 'admin/order.html', {'customer': customer, 'total': total - allSale})


def deleteCustomer(request, id_object):
    obj = Customer.objects.get(id=id_object)
    obj.delete()
    return HttpResponseRedirect('/admin/')


def set_category(request, id_object):
    obj = Catalog.objects.get(id=id_object)
    category = obj.category_set.all()
    return render(request, 'admin/category_set.html', {'category': category})


class In_category(View):
    def get(self, request, id_object):
        obj = Category.objects.get(id=id_object)
        category = obj.set_category.all()
        return render(request, 'admin/in_category.html', {'categories': category, 'category_title': obj})

    def post(self, request, id_object):
        category = Category.objects.get(id=id_object)
        obj = Category.objects.create(category=request.POST['category'])
        category.set_category.add(obj)

        return HttpResponse('да')


def all_sale(request):
    saleProduct = Product.objects.all().order_by('-sale')
    sale = saleProduct.exclude(sale=0)
    return render(request, 'admin/sales.html', {'sales': sale})


def search(request):
    search = request.GET['title']
    result = Product.objects.filter(title__icontains=search)
    return render(request, 'admin/search.html', {'result': result})
