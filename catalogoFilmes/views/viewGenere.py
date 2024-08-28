from rest_framework import generics
from catalogoFilmes.models import Genre
from catalogoFilmes.serializers import SerializerGenere
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalPermission



#View Read end Create
class ReadeCreateGenere(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,GlobalPermission,)
    queryset=Genre.objects.all()
    serializer_class = SerializerGenere

#view detail, update, delete
class GenereDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,GlobalPermission,)
    queryset=Genre.objects.all()
    serializer_class = SerializerGenere
