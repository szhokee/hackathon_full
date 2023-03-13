from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'py25 account project',
        f'http://localhost:8000/api/v1/account/activate/{code}/', #body
        'szhokee@gmail.com', #from
        [email]   # to
    )


def send_reset_password_code(email, code):
    send_mail(
        'py 25 shop',
        f'hello brosit parol = {code}',
        'szhokee@gmail.com',
        [email]
    )    