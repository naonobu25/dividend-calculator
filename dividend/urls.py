from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stock_manage, name='stock_manage'),
]
