from django.shortcuts import render
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from .models import Product, Category, Album
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    allProduct = Product.objects.all()
    return render(request, 'admin/index.html', {'products': allProduct})


def addPoduct(requset):
    return render(requset, 'admin/addProduct.html')


class ProductGetCreate(View):
    def get(self, request, id_product):
        allProduct = Product.objects.get(id=id_product)
        return render(request, 'admin/product.html', {'products': allProduct})

    def post(self, request):
        name = request.POST['name']
        desc = request.POST['description']
        photo = request.FILES['photo']
        if photo:
            myfile = request.FILES['photo']
            fs = FileSystemStorage(location='media/album')
            filename = fs.save(myfile.name, myfile)
            add = Product(photo='/album/' + filename, name=name, description=desc)
            add.save()
            return HttpResponse('вы добавили продукт')
