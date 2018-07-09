from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'gardyloo'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:country_id>', views.details, name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
