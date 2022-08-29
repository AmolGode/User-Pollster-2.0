import os
from celery import Celery
import requests


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_pollster.settings')

app = Celery('user_pollster')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def print_hello(self):
    print('Hello from celery')


@app.task(bind=True)
def delete_polls(self):
    resp = requests.delete(
        'http://127.0.0.1:8000/question_api/delete_24_hrs_old_questions/', data={}).json()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
