from django.urls import path
from .views import index, out

urlpatterns = [
    path('', index, name='index'),
    path('out', out, name='out'),
]