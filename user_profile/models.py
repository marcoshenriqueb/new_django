from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """docstring for UserProfile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    picture = models.CharField(max_length=100, blank=True, null=True)
    verified_token = models.CharField(max_length=100, blank=True, null=True)
    fb_id = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.picture)
