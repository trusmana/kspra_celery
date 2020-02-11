from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

class Visitor(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, null=False, related_name='visitor', on_delete=models.CASCADE)
    session_key = models.CharField(null=False, max_length=40)

    class Meta:
        db_table = 'visitor'
