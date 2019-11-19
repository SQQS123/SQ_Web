from django.db import models
from django.conf import settings
from django.utils import timezone
import os
import random


def user_portrait_upload_to(instance, filename):
    ext = os.path.splitext(filename)[1]
    fn = "%s_%s%s" % (timezone.now().strftime("%Y%m%d%H%M%S"),
                      random.randint(100000, 999999),
                      ext)
    return "portrait/%s" % fn


# Create your models here.
class Users(models.Model):
    class Meta:
        db_table = "users"
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    portrait = models.ImageField(upload_to=user_portrait_upload_to, default="images/default_portrait.jpg")

    def __str__(self):
        return self.username

    def get_portrait_url(self):
        if not self.portrait:
            return settings.MEDIA_URL + PORTRAIT_DEFAULT_PATH
        return self.portrait.url
