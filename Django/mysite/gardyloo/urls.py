from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int>:country_id', views.details, name='details')
]