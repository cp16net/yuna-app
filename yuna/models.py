from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser


class Schedule(models.Model):
    fields = ['user_id', 'schedule']


class User(AbstractUser):
    description = models.TextField(blank=True)
    picture_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)


admin.site.register(User)
admin.site.register(Schedule)
