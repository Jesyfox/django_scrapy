from celery import shared_task

from .models import MytheresaItem


@shared_task
def add_to_db(items):
    for item in items:
        new_model_item = MytheresaItem(**item)
        new_model_item.save()
    return f"added {len(items)} items"
