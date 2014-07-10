from django.contrib import admin
from django.db import models


class Schedule(models.Model):
    fields = ['user_id', 'schedule']


class User(models.Model):
    fields = ['username', 'email']

    def is_authenticated():
        return True

    def is_active():
        return True


admin.site.register(Schedule)
