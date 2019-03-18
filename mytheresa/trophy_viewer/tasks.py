from celery import shared_task

from .models import MytheresaItem

@shared_task
def add(x, y):
    print('aaa')
    return x + y

@shared_task
def add_to_db(val):
    print('adding to data base ', val)
