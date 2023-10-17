from . import views
from django.urls import path


urlpatterns = [
    path("<str:username>/add-playlists", views.AddPlaylistsView.as_view(), name="add_playlists"),
    path("<str:username>/discover", views.DiscoverView.as_view(), name="discover"),
    path("<str:username>/playlists", views.ProfilePlaylistsView.as_view(), name="profile_playlists"),
    path("<str:username>/playlist_<int:playlist_id>", views.PlaylistDetailsView.as_view(), name="playlist_details"),
    path("<str:username>/clubs", views.ClubView.as_view(), name="user_clubs"),
    path("<str:username>/clubs/<str:club_slug>", views.ClubDetailsView.as_view(), name="club_details"),
    path("<str:username>/clubs/<str:club_slug>/edit", views.ClubEditView.as_view(), name="club_edit"),
    path("<str:username>/settings", views.SettingsView.as_view(), name="user_settings"),
]
