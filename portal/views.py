from django.shortcuts import render, redirect, reverse,get_object_or_404
from .models import MessageChat, Subject
from profiles.models import UserProfile


def work_with_me(request):
    """ A view to return the reason page """

    return render(request, 'portal/work-with-me.html')


def portal(request):
    """ A view to return the reason page """
    messages = MessageChat.objects.all()
    topics = Subject.objects.all()
    topic_list = []
    for topic in topics:
        record = ["", ""]
        for message in messages:
            if message.subject == topic:
                if record[1] == "" or message.datetime > record[1]:
                    record = [topic, message.datetime]
        topic_list.append(record)

    if request.method == 'POST':

        profile = UserProfile.objects.get(user=request.user)
        topic = Subject.objects.create(message_subject=request.POST['subject'])
        subject = topic
        message = request.POST['message']
        obj = MessageChat(user_profile=profile, subject=subject, message=message)
        obj.save()
        return redirect(reverse('portal'))

    context = {
        'messages': topic_list,
    }

    return render(request, 'portal/portal.html', context)


def portal_replay(request, subject_id):
    messages = MessageChat.objects.all()
    topics = Subject.objects.all()
    topic_list = []
    for topic in topics:
        record = ["", ""]
        for message in messages:
            if message.subject == topic:
                if record[1] == "" or message.datetime > record[1]:
                    record = [topic, message.datetime]
        topic_list.append(record)
    conversation = messages.filter(subject=get_object_or_404(Subject, pk=subject_id))

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

    }

    return render(request, 'portal/portal.html', context)
