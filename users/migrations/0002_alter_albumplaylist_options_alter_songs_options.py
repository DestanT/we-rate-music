# Generated by Django 4.2.3 on 2023-09-11 12:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="albumplaylist",
            options={
                "ordering": ["-created_on"],
                "verbose_name_plural": "Album/Playlists",
            },
        ),
        migrations.AlterModelOptions(
            name="songs",
            options={"verbose_name_plural": "Songs"},
        ),
    ]
