from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import movie_list,movie_details
from .views import MovieListAV , MovieDetailAV


urlpatterns = [
    path('list/',MovieListAV.as_view() , name="movie-list"),
    path('<int:pk>/',MovieDetailAV.as_view() , name="movie-details")
]