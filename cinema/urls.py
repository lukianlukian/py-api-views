from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import MovieViewSet, GenreViewSet, ActorViewSet, CinemaHallViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path(
        "cinema-halls/",
        CinemaHallViewSet.as_view({"get": "list"}),
        name="cinema-hall-list"
    ),
]

app_name = "cinema"
