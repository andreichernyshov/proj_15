import time
from celery import shared_task


from django.core.mail import send_mail

from .models import Mesagesender


@shared_task
def save_field():
    time.sleep(10)
    fields = Mesagesender.objects.all()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for item in fields:
            f.write(item.name + '\n')


@shared_task
def send_mail_task(subject, when_to_do, email):
    send_mail(subject, when_to_do, ['zimacool@zimacool.com'], fail_silently=False)
    time.sleep(10)
