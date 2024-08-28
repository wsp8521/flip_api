from rest_framework import generics
from catalogoFilmes.serializers import ActorSerializer
from catalogoFilmes.models import Actor
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalPermission



#View Read end Create
class ActorCreateRead(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,GlobalPermission)
    queryset = Actor.objects.alias()
    serializer_class = ActorSerializer


#View Detail, update, delte
class ActorDeteilUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,GlobalPermission)
    queryset = Actor.objects.alias()
    serializer_class = ActorSerializer