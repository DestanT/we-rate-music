from django.db import models
from django.contrib.auth.models import User


class AlbumPlaylist(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="album_playlist"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Album/Playlists"

    def __str__(self):
        return self.title


class Songs(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album_playlist = models.ForeignKey(AlbumPlaylist, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Songs"
