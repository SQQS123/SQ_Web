# Generated by Django 2.2.4 on 2019-11-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='page',
            field=models.IntegerField(default=1),
        ),
    ]
