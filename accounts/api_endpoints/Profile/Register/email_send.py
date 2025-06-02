from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_email_confirmation(email, token):
    subject = "Confirm your email address"
    to_email = email
    context = {
        "token": token,
        "frontend_url": "eCommerce.com",
    }
    html_content = render_to_string("reset_password_email.html", context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()