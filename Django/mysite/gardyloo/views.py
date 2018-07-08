from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Country


def home(request):

    country = Country.objects.all()
    context = {
        'title': 'list of countries',
        'country': country
    }
    return render(request, 'gardyloo/home.html', context)

def details(request):

    country = Country.objects.all()
    context ={
        'country': country
    }
    return render(request, 'gardyloo/details.html',context)
