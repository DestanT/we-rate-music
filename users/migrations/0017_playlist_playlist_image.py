# Generated by Django 4.2.3 on 2023-09-27 17:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_rename_playlist_title_playlist_playlist_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
