from django.shortcuts import render
from django.views.generic import ListView

from .models import MytheresaItem


class Index(ListView):
    template_name = "trophy_viewer/index.html"

    model = MytheresaItem

    def post(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)
