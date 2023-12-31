from . import views
from django.urls import path


urlpatterns = [
    path("<str:username>/add-playlists", views.AddPlaylistsView.as_view(), name="add_playlists"),
    path("<str:username>/discover", views.DiscoverView.as_view(), name="discover"),
    path("<str:username>/playlists", views.ProfilePlaylistsView.as_view(), name="profile_playlists"),
    path("<str:username>/playlist_<int:playlist_id>", views.PlaylistDetailsView.as_view(), name="playlist_details"),
    path("<str:username>/clubs", views.ClubView.as_view(), name="user_clubs"),
    path("<str:username>/clubs/invitations", views.ClubInvitationsView.as_view(), name="club-invitations"),
    path("<str:username>/clubs/<str:club_slug>", views.ClubDetailsView.as_view(), name="club_details"),
    path("<str:username>/clubs/<str:club_slug>/edit", views.ClubEditView.as_view(), name="club_edit"),
    path("clubs/delete", views.delete_club, name="delete_club"),
    path("<str:username>/clubs/<str:club_slug>/handle-invite", views.handle_invitation, name="handle-invite"),
    path("<str:username>/settings", views.SettingsView.as_view(), name="user_settings"),
]
