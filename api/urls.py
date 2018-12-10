from django.urls import path
from api import views


urlpatterns = [
    path('', views.index, name='index'),
    path('card', views.card, name='card'),
    path('frontcard', views.frontcard, name='front'),
]
