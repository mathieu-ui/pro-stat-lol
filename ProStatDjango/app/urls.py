from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('masteries', masteries),
    path('match', match_view, name='match'),
    path('index', index),
    path('game/<str:game_code>', match_overview),
    path('action', redirector),
]