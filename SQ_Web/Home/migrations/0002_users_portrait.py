# Generated by Django 2.2.4 on 2019-11-11 05:36

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='portrait',
            field=models.ImageField(default='images/default_portrait.jpg', upload_to=Home.models.user_portrait_upload_to),
        ),
    ]