from django.urls import path
from . import adminView

urlpatterns = [
    path('', adminView.index, name='admin.index'),
]
