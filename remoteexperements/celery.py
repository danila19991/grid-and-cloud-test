import os
from celery import Celery
from sys import platform

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remoteexperements.settings')
if platform == 'win32':
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('remoteexperements')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
