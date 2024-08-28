from rest_framework import generics, views, response,status
from django.db.models import Avg, Count
from catalogoFilmes.models import Movie, Reviews
from catalogoFilmes.serializers import MovieSerializer, MovieSerializerGet
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalPermission


#View Read end Create
class MovieCreateRead(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset= Movie.objects.all()
    def get_serializer_class(self):

        if self.request.method == 'GET':
            return MovieSerializerGet
        return MovieSerializer

#view detail, update, delete
class MovieDeteilUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#Statistic of Movie
class StatisticMovie(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset= Movie.objects.all()

    def get(self, request):
        movie_by_genre = self.queryset.values('genre__name').annotate(count = Count('id'))
        total_Reviews = Reviews.objects.count()
        avg_stars = Reviews.objects.aggregate(Avg('stars'))['stars__avg']

        data = {
            'total_movies':self.queryset.count(),
            'movie_by_genre': movie_by_genre,
            'total_Reviews':total_Reviews,
            'avg_stars':round(avg_stars, 1)
            }
        return response.Response(data=data, status=status.HTTP_200_OK)