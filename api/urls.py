from django.urls import path
from api import views


urlpatterns = [
    path('', views.index, name='index'),
    path('card', views.card, name='card'),
    path('frontcard', views.frontcard, name='frontcard'),
    path('card/<int:pk>/', views.CardDetailView.as_view(),
         name='card_detail'),
    path('frontcard/<int:pk>/', views.FrontCardDetailView.as_view(),
         name='front_detail'),
]
