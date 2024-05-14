from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import MessageChat, Subject
from profiles.models import UserProfile


def work_with_me(request):
    """ A view to return the reason page """

    return render(request, 'portal/work-with-me.html')


@login_required
def portal(request):
    """ A view to return the reason page """
    profile = UserProfile.objects.get(user=request.user)
    if not profile.premium:
        return redirect(reverse('work_with_me'))

    is_coach = False;
    if request.user.groups.filter(name='coaches').exists():
        messages = MessageChat.objects.all()
        is_coach = True
    else:
        profile = UserProfile.objects.get(user=request.user)
        messages = MessageChat.objects.filter(user_profile=profile)

    topics = Subject.objects.all()
    topic_list = []
    for topic in topics:
        record = ["", "", ""]
        for message in messages:
            if message.subject == topic:
                if record[1] == "" or message.datetime > record[1]:
                    record[0] = topic
                    record[1] = message.datetime
                    record[2] = message.user_profile
        if record[1] != "":
            topic_list.append(record)

    if request.method == 'POST':

        profile = UserProfile.objects.get(user=request.user)
        topic = Subject.objects.create(message_subject=request.POST['subject'])
        message = request.POST['message']
        obj = MessageChat(user_profile=profile, subject=topic, message=message)
        obj.save()
        return redirect(reverse('portal'))

    context = {
        'messages': topic_list,
        'is_coach': is_coach,
    }

    return render(request, 'portal/portal.html', context)


@login_required
def portal_replay(request, subject_id):

    is_coach = False;
    if request.user.groups.filter(name='coaches').exists():
        messages = MessageChat.objects.all()
        is_coach = True
    else:
        profile = UserProfile.objects.get(user=request.user)
        messages = MessageChat.objects.filter(user_profile=profile)


    topics = Subject.objects.all()
    topic_list = []
    for topic in topics:
        record = ["", "", ""]
        for message in messages:
            if message.subject == topic:
                if record[1] == "" or message.datetime > record[1]:
                    record[0] = topic
                    record[1] = message.datetime
                    record[2] = message.user_profile
        if record[1] != "":
            topic_list.append(record)
    all_messages = MessageChat.objects.all()
    conversation = all_messages.filter(subject=get_object_or_404(Subject, pk=subject_id))

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        message = request.POST['message']
        subject = Subject.objects.get(pk=subject_id)
        MessageChat.objects.create(user_profile=profile, subject=subject, message=message)
        return redirect(reverse('portal'))

    context = {
        'messages': topic_list,
        'conversation': conversation,
        'id': subject_id,
        "is_coach": is_coach,
        "user": request.user,

    }

    return render(request, 'portal/portal.html', context)
