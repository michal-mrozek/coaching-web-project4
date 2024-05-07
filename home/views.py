from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def reasons(request):
    """ A view to return the reason page """

    return render(request, 'home/reasons.html')


def contact(request):
    """ A view to return the reason page """

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            name,
            surname,
            email,
            ["m.mrozek@hotmail.com"],
            fail_silently=False,
    )

    return render(request, 'home/contact.html')
