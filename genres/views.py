from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermission


class GenreCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
