from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from actors.models import Actor
from actors.serialiazers import ActorSerialiazer
from app.permissions import GlobalDefaultPermission

# Create your views here.


class ActorsListCreatView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialiazer


class ActorsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerialiazer
