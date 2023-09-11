from . import views
from django.urls import path


urlpatterns = [
    path("playlists/", views.PlaylistView.as_view(), name="profile"),
]
