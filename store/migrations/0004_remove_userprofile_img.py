# Generated by Django 4.0.4 on 2022-05-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_userprofile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='img',
        ),
    ]
