import logging
from typing import List

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException

from app.core.config import settings


logging.basicConfig(level=logging.INFO)


def send_mail(email_to: str, title: str, message: str):
    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_USERNAME
    msg["To"] = email_to
    msg["Subject"] = title
    body = MIMEText(message, "plain")
    msg.attach(body)

    try:
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            logging.info("Sending mail to %s", email_to)
            server.sendmail(settings.SMTP_USERNAME, email_to, msg.as_string())
    except Exception as error:
        raise HTTPException(
            status_code=500, detail=f"Error al enviar el correo: {str(error)}"
        )


def send_mails(emails: List[str], title: str, message: str):
    for email in emails:
        send_mail(email, title, message)
