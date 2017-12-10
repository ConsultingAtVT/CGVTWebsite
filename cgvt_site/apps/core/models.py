from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    li_email = models.TextField()
    li_first_name = models.CharField(max_length=50)
    li_last_name = models.CharField(max_length=50)
    li_picture_url = models.URLField()
    li_profile_url = models.URLField()
