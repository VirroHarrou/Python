from ast import Try
from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.urls import reverse 

from .models import Animal

# Create your views here.
def home(request):
    return HttpResponse('Главная страница')

def animals(request):
    try:
        animal_list = Animal.objects.order_by('id')[:10]
    except:
        raise Http404("Животное не найдено!")
    return render(request, 'Zoo/Animal.html',{'animal_list':animal_list})

def mapOfAnimals(request):
    return HttpResponse('Карта с местоположением клеток животных')