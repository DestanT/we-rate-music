from . import views
from django.urls import path


urlpatterns = [
    path(
        "<str:username>/playlists",
        views.PlaylistView.as_view(),
        name="user_playlists",
    ),
    path(
        "<str:username>/add-playlists",
        views.CreatePlaylistsView.as_view(),
        name="add_playlists",
    ),
    path("<str:username>/clubs", views.ClubView.as_view(), name="user_clubs"),
    path("<str:username>/settings", views.SettingsView.as_view(), name="user_settings"),
]
