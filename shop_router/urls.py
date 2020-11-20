from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('form/', views.form, name='form'),
    path('order/', views.order, name='order'),
    path('product/<int:id_obj>', views.product, name='product'),
    path('routers/<int:id_object>', views.routers, name='routers'),
    path('about/', views.about, name='about'),
    path('addProductToBascet/<int:id_object>', views.addProductToBascet, name='addProductToBascet'),
    path('addCount/<int:id_object>', views.addCountOrder, name='addCount'),
    path('minusCount/<int:id_object>', views.minusCountOrder, name='minusCount'),
    path('minusCount/<int:id_object>', views.minusCountOrder, name='minusCount'),
    path('category/<int:id_object>', views.category_set, name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('product-data/', views.DetailPopap.as_view(), name='product-data'),
    path('catalog-data/', views.CatalogAPi.as_view(), name='catalog-data'),
    path('category-data/', views.CategoryAPi.as_view(), name='category-data'),
    path('in-basket/', views.in_basket, name='in-basket'),
    path('count-order/', views.count_order, name='count_order'),

]
