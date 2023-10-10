# Generated by Django 4.2.3 on 2023-10-09 18:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_club_founder'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Club Image'),
        ),
    ]
