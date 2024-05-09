import uuid

from django.db import models
from profiles.models import UserProfile

class MessageChat(models.Model):
    """
    A user profile model for maintaining subscription information.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profile = models.ForeignKey('profiles.UserProfile', null=True, blank=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey('Subject', null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField()

    def __str__(self):
        return self.user_profile.user.username


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_subject = models.CharField(max_length=254)

    def __str__(self):
        return self.message_subject



