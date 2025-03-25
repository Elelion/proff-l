from django.urls import path
from . import views
from .views import *


app_name = 'home'


urlpatterns = [
    path('', HomeIndex.as_view(), name='index'),

    # **

    path('glazing/<int:pk>/', HomeGlazingFramelessDetail.as_view(), name='glazing_frameless_detail'),
    path('types/<int:pk>', HomeGlazingFramelessTypeDetail.as_view(), name='glazing_frameless_type_detail'),

    # **

    path('success_mail/', views.success_mail, name='success_mail'),
    path('feedback_modal/', views.feedback_modal, name='feedback_modal'),

    path('404/', views.page_not_found, name='page_not_found'),
]
