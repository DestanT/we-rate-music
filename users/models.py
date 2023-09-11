from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Playlist(models.Model):
    playlist_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_playlist"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.playlist_title


class Songs(models.Model):
    song_title = models.CharField(max_length=100)
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="playlist"
    )

    def __str__(self):
        return self.song_title
