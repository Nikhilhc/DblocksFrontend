from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from time import sleep


@shared_task
def send_mail_func(*args, **kwargs):
    print(args)
    mail_subject = "Task created"
    message = """New task has been created for you .Please check the details.\n
                    Leader Name: {}\n
                    Task Name: {}\n
                    Team Name: {}\n
                    Task Status:{}\n
                    Team Members:{}""".format(kwargs['team_leader_name'],kwargs['task_name'],
                                            kwargs['team_name'],
                                            kwargs['task_status'],kwargs['team_members'])
    to_email = kwargs['email']
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True
    )
    return "Done"