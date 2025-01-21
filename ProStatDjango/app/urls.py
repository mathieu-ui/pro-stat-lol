from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('out', out, name='out'),
    path('match', match_view, name='match'),
]