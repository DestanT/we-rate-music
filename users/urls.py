from . import views
from django.urls import path


urlpatterns = [
    path("playlists/<str:username>", views.PlaylistView.as_view(), name="user_profile"),
]
