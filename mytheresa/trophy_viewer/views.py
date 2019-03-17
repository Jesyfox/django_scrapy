from django.shortcuts import render
from django.views.generic import ListView

from .models import MytheresaItem
from .tasks import add


class Index(ListView):
    template_name = "trophy_viewer/index.html"

    model = MytheresaItem

    def post(self, request, *args, **kwargs):
        add.delay(1, 2)
        return self.get(self, request, *args, **kwargs)
