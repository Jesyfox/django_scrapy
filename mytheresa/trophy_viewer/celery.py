from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytheresa_dj.settings')

app = Celery('mytheresa_dj')
app.conf.broker_url = 'redis://localhost:6379/0'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# celery -A trophy_viewer worker -l info


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
