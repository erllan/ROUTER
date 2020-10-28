from django.urls import path
from . import adminView

urlpatterns = [
    path('', adminView.index, name='admin.index'),
    path('add/', adminView.ProductGetCreate.as_view(), name='add'),
    path('addProduct/', adminView.addPoduct, name='addProduct'),
]
