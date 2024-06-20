# map/views.py

from django.shortcuts import render

def mapCovid_view(request):
    return render(request, 'mapCovid.html')

def mapWar_view(request):
    return render(request, 'mapWar.html')

