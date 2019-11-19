from django.db import models
from django.conf import settings
from django.utils import timezone
import os
import random

def paints_upload_to(instance, filename):
    ext = os.path.splitext(filename)[1]
    fn = "%s_%s%s" % (timezone.now().strftime("%Y%m%d%H%M%S"),
                      random.randint(100000, 999999),
                      ext)
    return "paints/%s" % fn


# Create your models here.
class Comics(models.Model):
    class Meta:
        db_table = "comics"
    bookname = models.CharField(max_length=20)
    page = models.IntegerField(default=1)
    painter = models.ForeignKey(to="Home.Users", on_delete=models.CASCADE)
    paints = models.ImageField(upload_to=paints_upload_to)

    def get_paintsfile_url(self):
        if not self.paints:
            return settings.MEDIA_URL + PAINTS_DEFAULT_PATH
        return self.paints.url