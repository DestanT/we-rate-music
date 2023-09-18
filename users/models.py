from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField(
        "profile_image",
        null=True,
        blank=True,
        public_id="",
        overwrite=True,
        folder="we-rate-music/profiles",
    )
    background_image = CloudinaryField(
        "background_image",
        null=True,
        blank=True,
        public_id="",
        overwrite=True,
        folder="we-rate-music/backgrounds",
    )


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


class Club(models.Model):
    club_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through="MembersInClub")

    class Meta:
        verbose_name_plural = "Clubs"

    def __str__(self):
        return self.club_name


class MembersInClub(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["member", "club_name"]
