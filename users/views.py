from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.core.cache import cache
from django.contrib.auth.views import LoginView
from .models import UserProfile, Playlist, Track, Club, MembersInClub
from .forms import UserSettingsForm, ClubForm
from cloudinary.uploader import upload
from .spotify_api import get_access_token, get_user_playlists
import json


class HomepageView(TemplateView):
    template_name = "index.html"


class ProfilePlaylistsView(View):
    def get(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username
        my_playlists = Playlist.objects.filter(user=request.user)

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)
        viewed_playlists = Playlist.objects.filter(user=viewed_profile.user)

        return render(
            request,
            "users/playlists.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "my_playlists": my_playlists,
                "viewed_profile": viewed_profile,
                "viewed_playlists": viewed_playlists,
            },
        )
    

class PlaylistDetailsView(View):
    def get(self, request, username, playlist_id, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)
        viewed_playlists = Playlist.objects.get(user=viewed_profile.user, id=playlist_id)
        viewed_tracks = Track.objects.filter(playlist=viewed_playlists)

        return render(
            request,
            "users/playlist_details.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "viewed_profile": viewed_profile,
                "viewed_playlists": viewed_playlists,
                "viewed_tracks": viewed_tracks,
            },
        )


class AddPlaylistsView(View):
    def get(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)

        # If the user has Spotify username saved in DB; display public Spotify playlists
        if my_profile.spotify_username:
            cached_data_key = f"spotify_data_{my_username}"

            # Use cached data, if available
            spotify_playlists = cache.get(cached_data_key)

            if spotify_playlists is None:
                access_token = get_access_token()
                spotify_playlists = get_user_playlists(access_token, my_profile.spotify_username)
                
                # Save Spotify playlists to cache for 5 minutes
                cache.set(cached_data_key, spotify_playlists, 300)

            return render(
                request,
                "users/add_playlists.html",
                {
                    "my_profile": my_profile,
                    "my_username": my_username,
                    "viewed_profile": viewed_profile,
                    "spotify_playlists": spotify_playlists,
                    "playlist_added": False,
                },
            )
        
        # Else displays message for user; prompting to update Spotify username in "Settings"
        else:
            return render(
                request,
                "users/add_playlists.html",
                {
                    "my_profile": my_profile,
                    "my_username": my_username,
                    "viewed_profile": viewed_profile,
                    "missing_username": True,
                    "playlist_added": False,
                },
            )

    def post(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)

        # Add "Playlist" object
        playlist_name = request.POST.get("playlist_name")
        playlist_image = request.POST.get("playlist_image")

        if playlist_name:
            uploaded_image = upload(
                playlist_image,
                public_id=f"{username}_{playlist_name}",
                folder="we-rate-music/playlists",
            )

            new_playlist = Playlist.objects.create(
                playlist_name=playlist_name,
                user=request.user,
                playlist_image=uploaded_image["url"],
            )

            # Get all POST.items that start with "track=" and create "Song" objects with "Playlist" as PK
            for input_name, track_name in request.POST.items():
                if input_name.startswith("track="):
                    Track.objects.create(
                        track_name=track_name,
                        playlist=new_playlist,
                    )

        cached_data_key = f"spotify_data_{username}"
        spotify_playlists = cache.get(cached_data_key)

        return render(
            request,
            "users/add_playlists.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "viewed_profile": viewed_profile,
                "spotify_playlists": spotify_playlists,
                "missing_username": False,
                "playlist_added": True,
            },
        )


class DiscoverView(ListView):
    model = Playlist
    queryset = Playlist.objects.all()
    template_name = "users/discover.html"

    # Overwrites get_context_data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=self.request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        username = self.kwargs.get("username")
        viewed_profile = get_object_or_404(UserProfile, user__username=username)
        viewed_playlists = Playlist.objects.filter(user=viewed_profile.user)

        # Get all users from UserProfile model
        all_users = UserProfile.objects.all()
        users_list = [user.user.username for user in all_users]

        context["my_profile"] = my_profile
        context["my_username"] = my_username
        context["viewed_profile"] = viewed_profile
        context["viewed_playlists"] = viewed_playlists
        context["users_list"] = users_list
        return context


class ClubView(View):
    def get(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)
        viewed_clubs = MembersInClub.objects.filter(member=viewed_profile.user)

        return render(
            request,
            "users/clubs.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "viewed_profile": viewed_profile,
                "viewed_clubs": viewed_clubs,
            },
        )


class SettingsView(View):
    # Placeholder for Spotify username field
    def get_initial_form_data(self, user_profile):
        if user_profile.spotify_username:
             return {
                "spotify_username": user_profile.spotify_username
            }
        else:
            return {
                "spotify_username": "Enter your Spotify username"
            }

    def get(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username
        placeholder_data = self.get_initial_form_data(my_profile)

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)

        return render(
            request,
            "users/settings.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "viewed_profile": viewed_profile,
                "form": UserSettingsForm(initial=placeholder_data),
            },
        )

    def post(self, request, username, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)
        my_username = my_profile.user.username

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=username)
        settings_form = UserSettingsForm(request.POST, request.FILES)

        if settings_form.is_valid():
            spotify_username = settings_form.cleaned_data["spotify_username"]
            profile_image = settings_form.cleaned_data["profile_image"]
            background_image = settings_form.cleaned_data["background_image"]

            my_profile.spotify_username = spotify_username

            if profile_image:
                public_id = f"{username}_profile_image"
                uploaded_image = upload(
                    profile_image,
                    public_id=public_id,
                    folder="we-rate-music/profiles",
                )
                my_profile.profile_image = uploaded_image["url"]

            if background_image:
                public_id = f"{username}_background_image"
                uploaded_image = upload(
                    background_image,
                    public_id=public_id,
                    folder="we-rate-music/backgrounds",
                )
                my_profile.background_image = uploaded_image["url"]

            my_profile.save()

        placeholder_data = self.get_initial_form_data(my_profile)

        return render(
            request,
            "users/settings.html",
            {
                "my_profile": my_profile,
                "my_username": my_username,
                "viewed_profile": viewed_profile,
                "form": UserSettingsForm(initial=placeholder_data),
            },
        )
