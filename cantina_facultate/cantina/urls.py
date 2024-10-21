from django.urls import path
from cantina import views

urlpatterns = [
    path('', views.prima_pagina, name='prima_pagina'),
    path('meniu/', views.meniu, name='meniu'),
    path('contact/', views.contact, name='contact'),
]
