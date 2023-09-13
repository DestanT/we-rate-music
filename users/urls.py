from . import views
from django.urls import path


urlpatterns = [
    path(
        "<str:username>/playlists",
        views.PlaylistView.as_view(),
        name="profile_playlists",
    ),
    path("<str:username>/clubs", views.MusicClubView.as_view(), name="profile_clubs"),
]
