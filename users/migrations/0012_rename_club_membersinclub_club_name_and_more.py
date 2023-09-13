# Generated by Django 4.2.3 on 2023-09-13 11:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_club_membersinclub_club_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membersinclub',
            old_name='club',
            new_name='club_name',
        ),
        migrations.AlterUniqueTogether(
            name='membersinclub',
            unique_together={('member', 'club_name')},
        ),
    ]