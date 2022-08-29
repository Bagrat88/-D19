from django.core.mail import send_mail


def send(user_email):
    send_mail('Рассылка', 'News news', 'bhovsepyan88@gmail.com', [user_email], fail_silently=False,)
