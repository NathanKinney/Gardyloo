from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Country


def home(request):

    country = Country.objects.all()
    context = {
        'title': 'Country',
        'country': country
    }
    return render(request, 'gardyloo/home.html', context)

def details(request, country_id):

    country = Country.objects.get(pk=country_id)
    context = {
        'country':country
    }

    return render(request, 'gardyloo/details.html',context)

def quiz (request):

    return render(request, 'gardyloo/quiz.html')

def login (request):

    return render(request, 'gardyloo/login.html')