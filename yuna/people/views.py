import logging
import json

from django.http import Http404
from django.views.generic import detail

from yuna.models import User


class UserProfile(detail.DetailView):
    model = User
    slug_field = 'username'
    # context_object_name = 'profile'
    slug_url_kwarg = 'username'

    def get_object(self):
        obj = super(UserProfile, self).get_object()
        if not obj.is_active:
            raise Http404("User not found")
        return obj
