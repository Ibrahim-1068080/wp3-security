from django.urls import path
from . import views

urlpatterns = [
    path('api/onderzoeken/', views.onderzoek_create, name='onderzoek_create'),
]
