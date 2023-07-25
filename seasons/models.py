from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Seasons(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateField(default=date.today)

    WEEKS_PER_USER = [
        ("1", "1 Week"),
        ("2", "2 Weeks"),
        ("3", "3 Weeks"),
    ]
    weeks_per_user = models.CharField(max_length=1, choices=WEEKS_PER_USER, default=2)

    # end_date = groups.users*weeks_per_user  # NOTES: ADD END DATE FUNCTION
