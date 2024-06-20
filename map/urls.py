# map/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('mapCovid/', views.mapCovid_view, name='mapCovid'),
    path('mapWar/', views.mapWar_view, name='mapWar'),
]

