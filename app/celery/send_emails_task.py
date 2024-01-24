from celery import shared_task

from app.utils import send_mails

@shared_task
def send_mails_task(emails, title, message):
    send_mails(emails, title, message)
