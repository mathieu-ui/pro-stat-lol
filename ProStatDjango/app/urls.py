from django.urls import path
from .views import index, masteries

urlpatterns = [
    path('', index, name='index'),
    path('index', index),
    path('masteries', masteries),
]