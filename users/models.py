from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spotify_username = models.CharField(max_length=30, blank=True)
    profile_image = CloudinaryField(
        "Profile Image",
        null=True,
        blank=True,
        public_id="",
        overwrite=True,
        folder="we-rate-music/profiles",
    )
    background_image = CloudinaryField(
        "Background Image",
        null=True,
        blank=True,
        public_id="",
        overwrite=True,
        folder="we-rate-music/backgrounds",
    )


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    playlist_image = CloudinaryField(
        "Playlist Cover Image",
        null=True,
        blank=True,
        public_id="",
        folder="we-rate-music/playlists",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_playlist"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.playlist_name


class Track(models.Model):
    track_name = models.CharField(max_length=100)
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="playlist"
    )

    def __str__(self):
        return self.track_name


class Club(models.Model):
    club_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    club_image = CloudinaryField(
        "Club Image",
        null=True,
        blank=True,
        public_id="",
        overwrite=True,
        folder="we-rate-music/club-image",
    )
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="founder")
    date_created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through="MembersInClub")

    class Meta:
        verbose_name_plural = "Clubs"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.club_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.club_name
    

class MembersInClub(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE) ## NOTES: Fix this - it is club, not club_name

    class Meta:
        unique_together = ["member", "club_name"]


class ClubInvitation(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ["user", "club"]