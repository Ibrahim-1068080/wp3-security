from django.urls import path, include
from .views import ervaringsdeskundige_aanmaken_view, onderzoek_list, deelnemen, organisatie_profiel, genereer_api_key
from accounts import views
from . import views
from accounts.views import about2

urlpatterns = [
    path('', include('website.urls')),
    path('create/', ervaringsdeskundige_aanmaken_view, name='ervaringsdeskundige_create'),
    path('register/', ervaringsdeskundige_aanmaken_view, name='register'),
    path('onderzoeken/', onderzoek_list, name='onderzoek_list'),
    path('profiel/', views.ervaringsdeskundige_profiel, name='ervaringdeskundige_profiel'),
    path('accounts/organisatie/register/', views.organisatie_aanmaken_view, name='organisatie_register'),
    path('accounts/organisatie/profiel/', organisatie_profiel, name='organisatie_profiel'),
    path('organisatie/genereer_api_key/', genereer_api_key, name='genereer_api_key'),
    path('onderzoeken/deelnemen/<int:onderzoek_id>/', deelnemen, name='deelnemen_view'),
    path('profile/', views.profile, name='profile'),
    path('create_onderzoek/', views.create_onderzoek, name='create_onderzoek'),
    path('about/', views.about2, name='about'),
    path('deelnames/', views.deelname_lijst, name='deelname_lijst'),
    path('onderzoeken/verify/<int:onderzoek_id>/', views.verify_onderzoek, name='verify-onderzoek'),



]