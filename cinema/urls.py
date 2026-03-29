from django.urls import path

from cinema.views import MovieViewSet

movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
