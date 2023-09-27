from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import UserProfile, Playlist, Songs, Club, MembersInClub
from .forms import PlaylistForm, SongsForm, UserProfileImagesForm
from cloudinary.uploader import upload
from .spotify_api import get_access_token, get_user_playlists


class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user__username=username)
        playlists = Playlist.objects.filter(user=user_profile.user)

        return render(
            request,
            "users/playlists.html",
            {
                "user_profile": user_profile,
                "playlists": playlists,
            },
        )


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
            },
        )


class CreatePlaylistsView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)

        return render(
            request,
            "users/add_playlists.html",
            {
                "user_profile": user_profile,
            },
        )

    def post(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)

        search_query = request.POST.get("search_query")

        if search_query:
            access_token = get_access_token()
            search_results = get_user_playlists(access_token, search_query)

            return render(
                request,
                "users/add_playlists.html",
                {
                    "user_profile": user_profile,
                    "search_results": search_results,
                    "search_query": search_query,
                },
            )

        return render(
            request,
            "users/add_playlists.html",
            {
                "user_profile": user_profile,
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
