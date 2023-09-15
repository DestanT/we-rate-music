# Generated by Django 4.2.3 on 2023-09-15 19:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_club_membersinclub_club_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='background_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='background_image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='profile_image'),
        ),
    ]
