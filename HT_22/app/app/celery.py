import os
import sys
from os import path

import django
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
celery_app = Celery('scraper', broker='pyamqp://guest@localhost/')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

