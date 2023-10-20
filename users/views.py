from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.core.cache import cache
from .models import UserProfile, Playlist, Track, Club, MembersInClub, ClubInvitation
from .forms import UserSettingsForm, ClubForm, ClubInvitationForm
from cloudinary.uploader import upload
from .spotify_api import get_access_token, get_user_playlists


def get_base_template_data(request, **kwargs):
    """
    Gets username from the URL.
    Returns the UserProfile and Playlist objects of the viewed username.
    Both required to render base.html.
    """
    url_username = request.kwargs.get("username")
    viewed_profile = get_object_or_404(UserProfile, user__username=url_username)
    viewed_playlists = Playlist.objects.filter(user=viewed_profile.user)

    base_template_data = {
        "viewed_profile": viewed_profile,
        "viewed_playlists": viewed_playlists,
    }

    return base_template_data
    

class HomepageView(TemplateView):
    template_name = "base.html"


class ProfilePlaylistsView(View):
    def get(self, request, *args, **kwargs):
        base_template_data = get_base_template_data(self, **kwargs)
        my_playlists = Playlist.objects.filter(user=request.user)

        return render(
            request,
            "users/playlists.html",
            {
                "my_playlists": my_playlists,
                "viewed_profile": base_template_data["viewed_profile"],
                "viewed_playlists": base_template_data["viewed_playlists"],
            },
        )
    

class PlaylistDetailsView(View):
    def get(self, request, *args, **kwargs):
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        playlist = Playlist.objects.get(user=viewed_profile.user, id=self.kwargs.get("playlist_id"))
        tracks = Track.objects.filter(playlist=playlist)

        return render(
            request,
            "users/playlist_details.html",
            {
                "viewed_profile": viewed_profile,
                "playlist": playlist,
                "tracks": tracks,
            },
        )


class AddPlaylistsView(View):
    def get(self, request, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))

        # If the user has Spotify username saved in DB; display public Spotify playlists
        if my_profile.spotify_username:
            cached_data_key = f"spotify_data_{request.user.username}"

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
                    "viewed_profile": viewed_profile,
                    "missing_username": True,
                    "playlist_added": False,
                },
            )

    def post(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))

        # Add "Playlist" object
        playlist_name = request.POST.get("playlist_name")
        playlist_image = request.POST.get("playlist_image")

        if playlist_name:
            uploaded_image = upload(
                playlist_image,
                public_id=f"{request.user.username}_{playlist_name}",
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

        cached_data_key = f"spotify_data_{request.user.username}"
        spotify_playlists = cache.get(cached_data_key)

        return render(
            request,
            "users/add_playlists.html",
            {
                "viewed_profile": viewed_profile,
                "spotify_playlists": spotify_playlists,
                "missing_username": False,
                "playlist_added": True,
            },
        )


class DiscoverView(ListView):
    model = Playlist
    template_name = "users/discover.html"

    # Context needed to display page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Base template data
        base_template_data = get_base_template_data(self, **kwargs)

        # Get all UserProfile objects
        all_user_objects = UserProfile.objects.all()

        # URL to placeholder profile image on Cloudinary
        placeholder = "https://res.cloudinary.com/dxgzepuov/image/upload/v1694805348/we-rate-music/placeholder-user_swscgw.png"

        users_data = [
            {
                "username": user.user.username,
                "profile_image": user.profile_image.url if user.profile_image else placeholder
            }
            for user in all_user_objects
        ]

        context["viewed_profile"] = base_template_data["viewed_profile"]
        context["users_data"] = users_data

        return context


class ClubView(View):
    def get(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        viewed_clubs = Club.objects.filter(members=viewed_profile.user)

        return render(
            request,
            "users/clubs.html",
            {
                "viewed_profile": viewed_profile,
                "viewed_clubs": viewed_clubs,
                "form": ClubForm(),
            },
        )
    
    def post(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        viewed_clubs = Club.objects.filter(members=viewed_profile.user)

        form = ClubForm(request.POST, request.FILES)

        if form.is_valid():
            club_name = form.cleaned_data["club_name"]
            club_image = form.cleaned_data["club_image"]

            # Create the 'Club' object
            new_club = Club.objects.create(
                club_name=club_name,
                founder=self.request.user,
            )

            if club_image:
                uploaded_image = upload(
                    club_image,
                    public_id=f"{club_name}_club_image",
                    folder="we-rate-music/club-image",
                )

                new_club.club_image = uploaded_image["url"]
            else:
                new_club.club_image = "https://res.cloudinary.com/dxgzepuov/image/upload/v1696871384/we-rate-music/club-placeholder_ogz4pg.png"

            new_club.save()

            # Add founder in the members list of the club
            MembersInClub.objects.create(
                member=self.request.user,
                club_name=new_club
            )

            return render(
            request,
            "users/clubs.html",
            {
                "viewed_profile": viewed_profile,
                "viewed_clubs": viewed_clubs,
                "form": ClubForm(),
            },
        )


class ClubDetailsView(View):
    def get(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        viewed_club = Club.objects.get(members=viewed_profile.user, slug=self.kwargs.get("club_slug"))
        members = MembersInClub.objects.filter(club_name=viewed_club)

        return render(
            request,
            "users/club_details.html",
            {
                "viewed_profile": viewed_profile,
                "viewed_club": viewed_club,
                "members": members,
            },
        )
    

class ClubEditView(View):
    def get(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        viewed_club = Club.objects.get(members=viewed_profile.user, slug=self.kwargs.get("club_slug"))
        members = MembersInClub.objects.filter(club_name=viewed_club)
        invited_members = ClubInvitation.objects.filter(club=viewed_club, accepted=False)

        return render(
            request,
            "users/club_edit.html",
            {
                "viewed_profile": viewed_profile,
                "viewed_club": viewed_club,
                "members": members,
                "invited_members": invited_members,
                "form": ClubInvitationForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        viewed_club = Club.objects.get(members=viewed_profile.user, slug=self.kwargs.get("club_slug"))
        members = MembersInClub.objects.filter(club_name=viewed_club)
        invited_members = ClubInvitation.objects.filter(club=viewed_club, accepted=False)

        form = ClubInvitationForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data["user"]

            # Create a new invitation to user
            ClubInvitation.objects.create(
                club=viewed_club,
                user=user,
            )

            return render(
            request,
            "users/club_edit.html",
            {
                "viewed_profile": viewed_profile,
                "viewed_club": viewed_club,
                "members": members,
                "invited_members": invited_members,
                "form": ClubInvitationForm(),
            },
        )


def delete_club(request):
    if request.method == "POST":
        club_pk = request.POST.get("club_pk")
        club = get_object_or_404(Club, pk=club_pk)

        if request.user == club.founder:
            club.delete()

            return redirect("user_clubs", username=request.user.username)


class ClubInvitationsView(ListView):
    model = ClubInvitation
    template_name = "users/club_invitations.html"

    # Overwrites get_context_data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get details for username in the dynamic URL
        user_profile = get_object_or_404(UserProfile, user__username=self.request.user)
        club_invitations = ClubInvitation.objects.filter(user=self.request.user, accepted=False)

        context["viewed_profile"] = user_profile
        context["club_invitations"] = club_invitations

        return context


def handle_invitation(request, username, club_slug):
    if request.method == "POST":
        # "Next" value to redirect user back to where they came from
        next = request.POST.get("next")

        # ClubEditView - Club founders can delete any invitations
        viewed_club = Club.objects.get(slug=club_slug)
        if request.user == viewed_club.founder:
            username = request.POST.get("username")
            ClubInvitation.objects.filter(user__username=username, club=viewed_club).delete()

        # ClubInvitationsView - Logic for all other users receiving invitations
        else:
            accepted_club_id = request.POST.get("accepted")
            declined_club_id = request.POST.get("declined")

            # Add user to members of the club
            if accepted_club_id:
                club = get_object_or_404(Club, pk=accepted_club_id)

                MembersInClub.objects.create(
                member=request.user,
                club_name=club
            )
                
                # Change ClubInvitation.accepted to True
                club_invitation = get_object_or_404(ClubInvitation, club=club, user=request.user)
                club_invitation.accepted = True
                club_invitation.save()

            # Delete the ClubInvitation object
            if declined_club_id:
                ClubInvitation.objects.filter(user__username=request.user.username, club=viewed_club).delete()

        return redirect(next)


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

    def get(self, request, *args, **kwargs):
        placeholder_data = self.get_initial_form_data(request.user.userprofile)

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))

        return render(
            request,
            "users/settings.html",
            {
                "viewed_profile": viewed_profile,
                "form": UserSettingsForm(initial=placeholder_data),
            },
        )

    def post(self, request, *args, **kwargs):
        # Get currently logged-in user's details
        my_profile = get_object_or_404(UserProfile, user=request.user)

        # Get details for username in the dynamic URL
        viewed_profile = get_object_or_404(UserProfile, user__username=self.kwargs.get("username"))
        form = UserSettingsForm(request.POST, request.FILES)

        if form.is_valid():
            spotify_username = form.cleaned_data["spotify_username"]
            profile_image = form.cleaned_data["profile_image"]
            background_image = form.cleaned_data["background_image"]

            my_profile.spotify_username = spotify_username

            if profile_image:
                uploaded_image = upload(
                    profile_image,
                    public_id=f"{request.user.username}_profile_image",
                    folder="we-rate-music/profiles",
                )
                my_profile.profile_image = uploaded_image["url"]

            if background_image:
                uploaded_image = upload(
                    background_image,
                    public_id=f"{request.user.username}_background_image",
                    folder="we-rate-music/backgrounds",
                )
                my_profile.background_image = uploaded_image["url"]

            my_profile.save()

        # Get Spotify username data or default value to display in form
        placeholder_data = self.get_initial_form_data(my_profile)

        return render(
            request,
            "users/settings.html",
            {
                "my_profile": my_profile,
                "viewed_profile": viewed_profile,
                "form": UserSettingsForm(initial=placeholder_data),
            },
        )
