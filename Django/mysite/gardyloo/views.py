from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Country
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_register(request):
    next = request.GET.get('next', '')
    return render(request, 'gardyloo/login_register.html', {'next': next})

@login_required
def home(request):

    country = Country.objects.all()
    context = {
        'title': 'Country',
        'country': country
    }
    return render(request, 'gardyloo/home.html', context)

def user_registration(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('gardyloo:home'))

def user_login(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('gardyloo:home'))
    return HttpResponseRedirect(reverse('gardyloo:login_register'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('gardyloo:login_register'))

def details(request, country_id):

    country = Country.objects.get(pk=country_id)
    context = {
        'country':country
    }

    return render(request, 'gardyloo/details.html',context)

def quiz (request):

    return render(request, 'gardyloo/quiz.html')

# def login (request):
#
#     return render(request, 'gardyloo/login.html')