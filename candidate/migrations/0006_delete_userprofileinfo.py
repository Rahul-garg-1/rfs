# Generated by Django 2.2.6 on 2020-03-17 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_userprofileinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
