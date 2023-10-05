from . import views
from django.urls import path


urlpatterns = [
    path("<str:username>/playlists", views.ProfilePlaylistsView.as_view(), name="profile_playlists"),
    path("<str:username>/playlist_<int:playlist_id>", views.PlaylistDetailsView.as_view(), name="playlist_details"),
    path("<str:username>/add-playlists", views.AddPlaylistsView.as_view(), name="add_playlists"),
    path("<str:username>/clubs", views.ClubView.as_view(), name="user_clubs"),
    path("<str:username>/settings", views.SettingsView.as_view(), name="user_settings"),
]
