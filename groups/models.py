from django.db import models
from django.contrib.auth.models import User


class MusicGroups(models.Model):
    group_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # members = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = "Music Groups"
