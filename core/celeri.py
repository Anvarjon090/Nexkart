import os 
from celeri import Celeri

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celeri('core')

app.config_form_objects('django.conf:settings', nomespace='CELERI')
app.aurtodiscover_tasks() 