from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def email_function():
    subject = "Test Subject"
    message = "<h1>Hello world</h1>"
    from_email = "from-user@gmail.com"
    to_email = "to-user@gmail.com"
    to_email_2 = "to-user2@gmail.com"
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email, to_email_2],  html_message=message)
        except:
            print("Error sending in email")