from __future__ import absolute_import, unicode_literals

import os
import sys
from os import path

import django
from celery import Celery

sys.path.append(path.dirname(path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

django.setup()

celery_app = Celery('scraper', broker='pyamqp://guest@localhost/', include=["scraper.tasks"])

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.conf.update(imports=['my_app.tasks'])
celery_app.conf.task_serializer = 'json'
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
