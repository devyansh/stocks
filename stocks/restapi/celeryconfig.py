# celeryconfig.py
from celery import Celery

# Define the Celery app and its configuration
celery = Celery(
    'celery_worker',
    broker='redis://localhost:6379/0',
    include=['tasks.celery_worker']  # Include the 'tasks.celery_worker' module
)

# Set Celery configuration options
celery.conf.update(
    # Additional configuration options
)
