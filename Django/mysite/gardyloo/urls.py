from django.urls import path

from . import views

app_name = 'gardyloo'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:country_id>', views.details, name='details'),
    path('quiz/', views.quiz, name='quiz'),
    path('login/', views.login, name='login'),
]