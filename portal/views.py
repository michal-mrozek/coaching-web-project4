from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .models import MessageChat
from profiles.models import UserProfile


def work_with_me(request):
    """ A view to return the reason page """

    return render(request, 'portal/work-with-me.html')


@login_required
def portal(request):
    """ A view to return the reason page """
    profile = UserProfile.objects.get(user=request.user)
    topics = set(MessageChat.objects.values_list('subject'))
    if not profile.premium:
        return redirect(reverse('work_with_me'))

    is_coach = False;
    if request.user.groups.filter(name='coaches').exists():
        query = []
        messages = MessageChat.objects.all()
        is_coach = True
    else:
        query = []
        print(topics)
        for topic in topics:
            messages = list(MessageChat.objects.filter(user_profile=profile, subject=topic[0]).order_by('-datetime').values())
            query.append(messages)

    if request.method == 'POST':

        profile = UserProfile.objects.get(user=request.user)
        subject = request.POST['subject']
        message = request.POST['message']
        obj = MessageChat(user_profile=profile, subject=subject, message=message)
        obj.save()
        return redirect(reverse('portal'))

    context = {
        'messages': query,
        'subjects': topics,
        'is_coach': is_coach,
    }

    return render(request, 'portal/portal.html', context)


@login_required
def portal_replay(request, passed_topic):
    profile = UserProfile.objects.get(user=request.user)
    topics = set(MessageChat.objects.values_list('subject'))
    if not profile.premium:
        return redirect(reverse('work_with_me'))

    is_coach = False;
    if request.user.groups.filter(name='coaches').exists():
        query = []
        messages = MessageChat.objects.all()
        is_coach = True
    else:
        query = []
        print(topics)
        for topic in topics:
            messages = list(
                MessageChat.objects.filter(user_profile=profile, subject=topic[0]).order_by('-datetime').values())
            query.append(messages)

    conversation = MessageChat.objects.filter(subject=passed_topic)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        message = request.POST['message']
        subject = passed_topic
        MessageChat.objects.create(user_profile=profile, subject=subject, message=message)
        return redirect(reverse('portal'))

    context = {
        'messages': query,
        'conversation': conversation,
        "is_coach": is_coach,
        "user": request.user,

    }

    return render(request, 'portal/portal.html', context)
