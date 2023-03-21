from celery import shared_task
from django.core.mail import send_mail
from decouple import config

@shared_task
def send_ticket_confirmation_code(email, code, name, price):
    full_link = f'Hi, confirm your order of {name} total price: {price}\n\n http://localhost:8000/api/v1/ticket/confirm/{code}'

    send_mail(
        'Ticket from ticket kg',
        full_link,
        config('EMAIL_HOST_USER'),
        [email]
    )
