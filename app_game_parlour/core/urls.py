from django.urls import path

from core.views import player_list_view, player_detail_view

urlpatterns = [
    path("players/", player_list_view, name="players-list"),
    path("players/<int:pk>/", player_detail_view, name="player-details"),
]
