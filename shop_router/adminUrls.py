from django.urls import path
from . import adminView

urlpatterns = [
    path('', adminView.index, name='admin.index'),
    path('add/', adminView.ProductDeleteCreate.as_view(), name='add'),
    path('delete/<int:id_object>', adminView.ProductDeleteCreate.as_view(), name='delete'),
    path('product/', adminView.allProduct, name='products'),
    path('category/', adminView.all_category, name='category'),
    path('category/<int:object_id>', adminView.CreateDeleteCategory, name='deleteCategory'),
    path('createCategory/', adminView.CreateDeleteCategory.as_view(), name='createCategory'),
    path('CategoryDelete/<int:id_object>', adminView.CreateDeleteCategory.as_view(), name='CategoryDelete'),
    path('form/', adminView.productForm, name='productForm'),
    path('brand/', adminView.BrandListCreate.as_view(), name='brand'),
    path('brand/<int:id_object>', adminView.deleteBrand, name='deleteBrand'),
    path('product/<int:id_object>', adminView.DetailProductAndCreateAlbum.as_view(), name='detailProduct'),
    path('category_set/<int:id_object>', adminView.category_set, name='category_set'),
]
