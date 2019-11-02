from django.db import models


# Create your models here.
class UsersInfo(models.Model):
    class Meta:
        db_table = "users"

