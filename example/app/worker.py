import os
from celery import Celery

CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', 'redis://backend:6379'),
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://backend:6379')

task_queue = Celery('tasks', broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND)
