from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.BoysCatalog.as_view(), name='index'),
    ]
