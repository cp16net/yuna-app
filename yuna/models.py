from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser


class Schedule(models.Model):
    fields = ['user_id', 'schedule']


class User(models.Model):
    fields = ['username', 'email']

    def is_authenticated():
        return True

    def is_active():
        return True


# class CustomUser(AbstractUser):
#     pass


admin.site.register(Schedule)
