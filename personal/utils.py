from celery.task import task
from django.core.mail import send_mail


@task(name='ps.personal.tasks.send_mail_async')
def send_mail_async(subject=None, message=None, from_email=None, recipient_list=None):
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
