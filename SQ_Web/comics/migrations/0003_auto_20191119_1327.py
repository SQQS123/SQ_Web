# Generated by Django 2.2.4 on 2019-11-19 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_comics_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comics',
            old_name='bookename',
            new_name='bookname',
        ),
    ]
