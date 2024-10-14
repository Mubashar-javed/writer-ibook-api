from django.db import models

from django.contrib.auth import get_user_model
from .enums import ProjectStatus


User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(
        max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.PENDING
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
