from celery import Celery
import os


# set the default Django settings module for the 'celery' progam

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app= Celery('myshop')
app.config_from_object('django.conf:settings', namespace= 'CELERY')
app.autodiscover_tasks()