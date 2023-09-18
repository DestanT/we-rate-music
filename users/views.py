from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import UserProfile, Playlist, Club, MembersInClub
from .forms import PlaylistForm, UserProfileImagesForm
from cloudinary.uploader import upload


class PlaylistView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        return render(
            request,
            "users/playlists.html",
            {
                "user_profile": user_profile,
                "playlists": playlists,
                "playlist_form": PlaylistForm(),
            },
        )

    def post(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        playlist_form = PlaylistForm(data=request.POST)

        if playlist_form.is_valid():
            new_playlist = playlist_form.save(commit=False)
            new_playlist.user = user_profile.user
            new_playlist.save()
        else:
            playlist_form = PlaylistForm()

        return render(
            request,
            "users/playlists.html",
            {
                "user_profile": user_profile,
                "playlists": playlists,
                "playlist_form": PlaylistForm(),
            },
        )


class ClubView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        clubs = MembersInClub.objects.filter(member=user_profile.user)

        return render(
            request,
            "users/clubs.html",
            {"user_profile": user_profile, "clubs": clubs},
        )


class SettingsView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)

        return render(
            request,
            "users/settings.html",
            {
                "user_profile": user_profile,
                "image_form": UserProfileImagesForm(),
            },
        )

    def post(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        image_form = UserProfileImagesForm(request.POST, request.FILES)

        if image_form.is_valid():
            profile_image = image_form.cleaned_data["profile_image"]
            background_image = image_form.cleaned_data["background_image"]

            if profile_image:
                public_id = f"{username}_profile_image"
                uploaded_image = upload(
                    profile_image,
                    public_id=public_id,
                    folder="we-rate-music/profiles",
                )
                user_profile.profile_image = uploaded_image["public_id"]

            if background_image:
                public_id = f"{username}_background_image"
                uploaded_image = upload(
                    background_image,
                    public_id=public_id,
                    folder="we-rate-music/backgrounds",
                )
                user_profile.background_image = uploaded_image["public_id"]

            user_profile.save()

        return render(
            request,
            "users/settings.html",
            {
                "user_profile": user_profile,
                "image_form": UserProfileImagesForm(),
            },
        )
