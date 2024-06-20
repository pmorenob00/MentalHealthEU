# questionnaire/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire2014/', views.questionnaire2014_view, name='questionnaire2014'),
    path('questionnaire2023/', views.questionnaire2023_view, name='questionnaire2023'),
    path('questionnaireCOVID/', views.questionnaireCOVID_view, name='questionnaireCOVID'),
    path('comparative2023vs2014/', views.comparative2023vs2014_view, name='comparative2023vs2014'),
    path('comparativeMHvsOP/', views.comparativeMHvsOP_view, name='comparativeMHvsOP'),
    path('stigmaGeneral/', views.stigmaGeneral_view, name='stigmaGeneral'),
    path('stigmaSpecific/', views.stigmaSpecific_view, name='stigmaSpecific'),
    # Add other URL patterns if needed
]
