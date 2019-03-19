import redis

from django.views.generic import TemplateView

from .models import MytheresaItem, Category


class BoysCatalog(TemplateView):
    template_name = "trophy_viewer/boys_catalog.html"
    url = 'https://www.mytheresa.com/en-us/boys.html'
    spider = 'boys_catalog'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis_db = redis.Redis()

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(categories=Category.objects.all(),
                       object_list=MytheresaItem.objects.filter(category__name="boys_catalog"))
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        kwargs.update(started_scrapy=True)
        self.redis_db.lpush('{spider}:start_urls'.format(spider=self.spider), self.url)
        return self.get(self, request, *args, **kwargs)
