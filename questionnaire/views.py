# questionnaire/views.py

from django.shortcuts import render

def questionnaire2014_view(request):
    return render(request, 'questionnaire2014.html')

def questionnaire2023_view(request):
    return render(request, 'questionnaire2023.html')

def questionnaireCOVID_view(request):
    return render(request, 'questionnaireCOVID.html')

def comparative2023vs2014_view(request):
    return render(request, 'comparative2023vs2014.html')

def comparativeMHvsOP_view(request):
    return render(request, 'comparativeMHvsOP.html')

def dashboardComparative_view(request):
    return render(request, 'dashboardComparative.html')

def dashboardComparativeMHvsOP_view(request):
    return render(request, 'dashboardComparativeMHvsOP.html')

def stigmaGeneral_view(request):
    return render(request, 'stigmaGeneral.html')

def stigmaSpecific_view(request):
    return render(request, 'stigmaSpecific.html')

def dashboardStigmaGeneral_view(request):
    return render(request, 'dashboardStigmaGeneral.html')

def dashboardStigmaSpecific_view(request):
    return render(request, 'dashboardStigmaSpecific.html')



