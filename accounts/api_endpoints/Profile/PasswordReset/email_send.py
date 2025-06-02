import ssl
import certifi
from django.core.mail import get_connection, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_password_reset_email(email, token):
    subject = "Parolingizni tiklash"
    context = {
        "token": token,
        "frontend_url": "voocommerce.com",
    }
    html_content = render_to_string("reset_password_email.html", context)

    # SSL konteksni certifi orqali o‘rnatamiz
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    connection = get_connection(
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=True,
        ssl_context=ssl_context
    )

    email_message = EmailMessage(
        subject,
        html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
        connection=connection
    )
    email_message.content_subtype = "html"
    email_message.send()