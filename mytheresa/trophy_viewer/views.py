import redis

from django.shortcuts import render
from django.views.generic import ListView

from .models import MytheresaItem


class Index(ListView):
    template_name = "trophy_viewer/index.html"

    model = MytheresaItem

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis_db = redis.Redis()

    def post(self, request, *args, **kwargs):
        self.redis_db.lpush('boys_catalog:start_urls', 'https://www.mytheresa.com/en-us/boys.html?block=boys')
        return self.get(self, request, *args, **kwargs)
