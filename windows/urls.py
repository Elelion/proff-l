from django.urls import path
from . import views


app_name = 'windows'


urlpatterns = [
    path('', views.index, name='index'),
]
