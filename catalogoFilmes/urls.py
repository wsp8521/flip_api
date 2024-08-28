from django.urls import path
from catalogoFilmes import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
  

    #AUTHENTICATION TOKEN
    path('authentication/token', TokenObtainPairView.as_view(), name='token_obtain_pair' ), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #ENDPOINT GENERE
    path('genere/', views.ReadeCreateGenere.as_view(), name='genere_create_read' ),    #Read and crete
    path('genere/<int:pk>', views.GenereDetailUpdateDelete.as_view(), name='genere_detail_Up_delete' ),    #Detail, update, delete

    #ENDPOINT ACTORS
    path('actor/', views.ActorCreateRead.as_view(), name='actor_create_read' ),  
    path('actor/<int:pk>', views.ActorDeteilUpdateDelete.as_view(), name='Actor_detail_Up_delete' ),  

    #ENDPOINT MOVIE
    path('movie/', views.MovieCreateRead.as_view(), name='movie_create_read' ),  
    path('movie/statistic/', views.StatisticMovie.as_view(), name='movie_statistic' ),
    path('movie/<int:pk>', views.MovieDeteilUpdateDelete.as_view(), name='movie_detail_Up_delete' ),
    path('movie/<int:pk>', views.MovieDeteilUpdateDelete.as_view(), name='movie_detail_Up_delete' ),


    #ENDPOINT REVIEW
    path('review/', views.ReviewsCreateRead.as_view(), name='actor_create_read' ),  
    path('review/<int:pk>', views.ReviewsDeteilUpdateDelete.as_view(), name='Actor_detail_Up_delete' ),  

]
