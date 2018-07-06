from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Country, Language, CountryLanguage, Religion, CountryReligion, Article
def index(request):
    return HttpResponse("Hello, world. You're at the gardyloo index.")