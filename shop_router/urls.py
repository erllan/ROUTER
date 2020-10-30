from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('form/', views.form, name='form'),
    path('order/', views.order, name='order'),
    path('product/<int:id_obj>', views.product, name='product'),
    path('routers/', views.routers, name='routers'),
    path('about/', views.about, name='about'),
    path('addProductToBascet/<int:id_object>', views.addProductToBascet, name='addProductToBascet'),
]
