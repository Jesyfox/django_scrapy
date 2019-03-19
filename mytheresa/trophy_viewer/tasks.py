from celery import shared_task

from .models import MytheresaItem, Category


@shared_task
def add_to_db(items):
    for item in items:
        category_model, created = Category.objects.get_or_create(name=item['category'])
        item.update(category=category_model)
        new_model_item = MytheresaItem(**item)
        new_model_item.save()
    return f"added {len(items)} items"
