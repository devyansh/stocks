# celeryconfig.py
from celery import Celery

# Define the Celery app and its configuration
app = Celery(
    'celeryconfig',
    broker='redis://localhost:6379/0',
    backend="redis://localhost:6379/0",
    include=['tasks.celery_worker']  # Include the 'tasks.celery_worker' module
)

# Set the log level to debug
app.conf.update(
    CELERYD_LOG_LEVEL='debug'
)
