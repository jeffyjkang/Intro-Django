from django.db import models
# python library for uuid
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
# After Note app is created, must go into project, under settings and inform project Installed_apps that this app is available
class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)