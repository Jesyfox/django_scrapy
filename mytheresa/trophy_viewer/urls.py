from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    ]
