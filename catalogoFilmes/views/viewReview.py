from rest_framework import generics
from catalogoFilmes.models import Reviews
from catalogoFilmes.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalPermission


#View Read end Create
class ReviewsCreateRead(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset= Reviews.objects.all()
    serializer_class = ReviewSerializer

#view detail, update, delete
class ReviewsDeteilUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
