import os
from celery import Celery
from celery.schedules import crontab


TIME_ZONE = 'Asia/Bishkek'


app = Celery('myapp', broker='amqp://guest@localhost//', backend='rpc://')
app.autodiscover_tasks()
app.conf.timezone = TIME_ZONE


app.conf.beat_schedule = {
    'send_msg_day-every-hour': {
        'task': 'main.tasks.send_msg_day',
        'schedule': crontab(hour='*/1')
    },
}