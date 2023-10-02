from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.cache import cache
from .models import UserProfile, Playlist, Songs, Club, MembersInClub
from .forms import UserSettingsForm
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
    

class PlaylistDetailsView(View):
    def get(self, request, username, playlist_id, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user__username=username)
        playlist = Playlist.objects.get(user=user_profile.user, id=playlist_id)
        tracks = Songs.objects.filter(playlist=playlist)

        return render(
            request,
            "users/playlist_details.html",
            {
                "user_profile": user_profile,
                "playlist": playlist,
                "tracks": tracks,
            },
        )


class AddPlaylistsView(View):
    def get(self, request, username, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user__username=username)

        # If the user has Spotify username saved in DB; display public Spotify playlists
        if user_profile.spotify_username:
            cached_data_key = f"spotify_data_{username}"

            # Use cached data, if available
            spotify_playlists = cache.get(cached_data_key)

            if spotify_playlists is None:
                access_token = get_access_token()
                spotify_playlists = get_user_playlists(access_token, user_profile.spotify_username)
                
                # Save Spotify playlists to cache for 5 minutes
                cache.set(cached_data_key, spotify_playlists, 300)

            return render(
                request,
                "users/add_playlists.html",
                {
                    "user_profile": user_profile,
                    "spotify_playlists": spotify_playlists,
                },
            )
        
        # Else displays message for user; prompting to update Spotify username in "Settings"
        else:
            missing_username = True
            return render(
                request,
                "users/add_playlists.html",
                {
                    "user_profile": user_profile,
                    "missing_username": missing_username,
                },
            )

    def post(self, request, username, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user__username=username)

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
                    Songs.objects.create(
                        track_name=track_name,
                        playlist=new_playlist,
                    )

        cached_data_key = f"spotify_data_{username}"
        spotify_playlists = cache.get(cached_data_key)

        return render(
            request,
            "users/add_playlists.html",
            {
                "user_profile": user_profile,
                "spotify_playlists": spotify_playlists,
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
        user_profile = get_object_or_404(UserProfile, user__username=username)
        placeholder_data = self.get_initial_form_data(user_profile)

        return render(
            request,
            "users/settings.html",
            {
                "user_profile": user_profile,
                "image_form": UserSettingsForm(initial=placeholder_data),
            },
        )

    def post(self, request, username, *args, **kwargs):
        user_profile = UserProfile.objects.get(user__username=username)
        settings_form = UserSettingsForm(request.POST, request.FILES)

        if settings_form.is_valid():
            spotify_username = settings_form.cleaned_data["spotify_username"]
            profile_image = settings_form.cleaned_data["profile_image"]
            background_image = settings_form.cleaned_data["background_image"]

            user_profile.spotify_username = spotify_username

            if profile_image:
                public_id = f"{username}_profile_image"
                uploaded_image = upload(
                    profile_image,
                    public_id=public_id,
                    folder="we-rate-music/profiles",
                )
                user_profile.profile_image = uploaded_image["url"]

            if background_image:
                public_id = f"{username}_background_image"
                uploaded_image = upload(
                    background_image,
                    public_id=public_id,
                    folder="we-rate-music/backgrounds",
                )
                user_profile.background_image = uploaded_image["url"]

            user_profile.save()

        placeholder_data = self.get_initial_form_data(user_profile)

        return render(
            request,
            "users/settings.html",
            {
                "user_profile": user_profile,
                "image_form": UserSettingsForm(initial=placeholder_data),
            },
        )
