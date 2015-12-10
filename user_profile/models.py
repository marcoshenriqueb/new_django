from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """docstring for UserProfile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=100, null=True)
    verified_token = models.CharField(max_length=100, null=True)
    fb_id = models.CharField(max_length=100, null=True)
