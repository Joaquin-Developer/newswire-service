from celery import Celery

app = Celery("test_newswire_service")
app.autodiscover_tasks()
