from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(APIView):
    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)


class ActorViewSet(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        actors = self.get_queryset()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)


class CinemaHallViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
