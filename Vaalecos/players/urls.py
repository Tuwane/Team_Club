from django.urls import path
from . import views


urlpatterns = [
    path('', views.players, name = 'main'),
    path('players/' , views.players, name='players'),
    path('players/details/<int:id>', views.details, name ='details'),
]
