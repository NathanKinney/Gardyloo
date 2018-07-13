from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Country, Question, QuestionAnswer
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Max
import random
from random import shuffle
import re

def login_register(request):
    next = request.GET.get('next', '')
    return render(request, 'gardyloo/login_register.html', {'next': next})

@login_required
def home(request):

    countries = Country.objects.all()
    context = {
        'title': 'Country',
        'countries': countries
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


# 1) pick a random question
# 2) pick a random country, use to replace the text in question and pick the correct answer
# 1) randomly pick 3 other unique answers for that particular question
def quiz (request):

    return render(request, 'gardyloo/quiz.html')

def quiz_question(request):

    # get a random country
    #country = random.choice(Country.objects.all())

    # get a random question
    question = random.choice(Question.objects.all())

    # get random answers
    # answers = QuestionAnswer.objects.filter(question_id=question.id, )
    all_answers = list(question.answers.all())
    # random.shuffle(answers)

    # answers_text = [answer.text for answer in answers]

    answers = []
    for i in range(4):
        while True:
            # get random answer
            answer = random.choice(all_answers)
            # check if answer's in list of answers
            is_unique = True
            for a in answers:
                if a.text == answer.text:
                    is_unique = False
                    break
            if is_unique:
                answers.append(answer)
                break

    print(answers)

    country = answers[0].country
    question_text = question.text.replace('[country]', country.name)
    # can only call an attribute when its a single element
    answers = [answer.text for answer in answers]
    correct_answer = answers[0]
    random.shuffle(answers)
    correct_index = answers.index(correct_answer)

    data = {
        'question': question_text,
        'answer': answers,
        'correct_answer_index': correct_index
    }



    return JsonResponse(data)
