from django.urls import path
from . import adminView

urlpatterns = [
    path('', adminView.index, name='admin.index'),
    path('login/', adminView.login_admin, name='login'),
    path('logout/', adminView.admin_logout, name='logout'),
    path('add/', adminView.ProductDeleteCreate.as_view(), name='add'),
    path('delete/<int:id_object>', adminView.ProductDeleteCreate.as_view(), name='delete'),
    path('product/', adminView.allProduct, name='products'),
    path('add/form/<int:id_objects>', adminView.productForm, name='productForm'),
    path('brand/', adminView.BrandListCreate.as_view(), name='brand'),
    path('brand/<int:id_object>', adminView.deleteBrand, name='deleteBrand'),
    path('product/<int:id_object>', adminView.DetailProductAndCreateAlbum.as_view(), name='detailProduct'),
    path('order/<int:id_object>', adminView.order, name='order'),
    path('addSale/<int:id_object>', adminView.sale, name='addSale'),
    path('create/', adminView.catalog, name='catalog'),
    path('catalogs/', adminView.createCatalog, name='catalogs'),
    path('catalog/<int:id_object>', adminView.getCatalog, name='getCatalog'),
    path('category/<int:id_object>', adminView.detailCategory, name='detailCategory'),
    path('deleteCategory/<int:id_object>', adminView.deleteCategory, name='deleteCategory'),
    path('deleteCatalog/<int:id_object>', adminView.deleteCatalog, name='deleteCatalog'),
    path('album/<int:id_object>', adminView.AddDeleteAlbum.as_view(), name='addAlbum'),
    path('customer/<int:id_object>', adminView.deleteCustomer, name='deleteCustomer'),
    path('hit/<int:id_object>', adminView.hit, name='addToHit'),
    path('hit/', adminView.hits, name='hits'),
    path('category_set/<int:id_object>', adminView.set_category, name='category_set'),
    path('in_category/<int:id_object>', adminView.In_category.as_view(), name='in_category'),
]
