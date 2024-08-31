from django.core.mail import EmailMessage ,BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'from@farzan.com', ['to@farzan.com'])
        message.attach_file('playground/static/images/entity.jpeg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
