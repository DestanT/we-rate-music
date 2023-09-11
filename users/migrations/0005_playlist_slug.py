# Generated by Django 4.2.3 on 2023-09-11 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
