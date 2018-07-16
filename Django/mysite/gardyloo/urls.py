from django.urls import path

from . import views

app_name = 'gardyloo'

urlpatterns = [
    path('', views.home, name='home'),
    path('login_register/',views.login_register, name='login_register'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_registration, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_question/', views.quiz_question, name='quiz_question'),
    path('details/<int:country_id>', views.details, name='details'),
    path('home_page/', views.home_page, name='home_page'),
    path('search/', views.search, name='search'),
]
