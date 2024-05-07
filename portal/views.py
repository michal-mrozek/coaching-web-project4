from django.shortcuts import render
from .models import MessageChat
from profiles.models import UserProfile


# Create your views here.
def work_with_me(request):
    """ A view to return the reason page """

    return render(request, 'portal/work-with-me.html')


def portal(request):
    """ A view to return the reason page """
    messages = MessageChat.objects.all()
    mydata = MessageChat.objects.values_list('subject')

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        subject = request.POST['subject']
        message = request.POST['message']
        obj = MessageChat(user_profile=profile, subject=subject, message=message)
        obj.save()

    context = {
        'messages': messages,
        'mydata': mydata,
    }

    return render(request, 'portal/portal.html', context)

# def portal_replay(request, subject):
#     if request.method == 'POST':
#         profile = UserProfile.objects.get(user=request.user)
#         message = request.POST['message']
#         obj = MessageChat.objects.get(user_profile=profile, subject=subject , message=message)
#         obj.save()


