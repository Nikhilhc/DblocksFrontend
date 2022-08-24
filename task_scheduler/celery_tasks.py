from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from time import sleep


@shared_task
def send_mail_func(*args, **kwargs):
    print(args)
    mail_subject = "Task created"
    message = "New task has been created for you .Please check and assign.."
    to_email = kwargs['email']
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True
    )
    return "Done"