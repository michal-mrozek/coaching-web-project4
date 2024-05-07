from django.shortcuts import render


# Create your views here.
def work_with_me(request):
    """ A view to return the reason page """

    return render(request, 'portal/work-with-me.html')
