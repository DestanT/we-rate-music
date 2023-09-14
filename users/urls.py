from . import views
from django.urls import path


urlpatterns = [
    path(
        "<str:username>/playlists",
        views.PlaylistView.as_view(),
        name="user_playlists",
    ),
    path("<str:username>/clubs", views.ClubView.as_view(), name="user_clubs"),
]
