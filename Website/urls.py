from django.urls import path, include
from website import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from accounts.views import custom_login
from .views import home_view, custom_logout
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', views.about, name='about'),
    path('test', views.test, name='test'),
    path('login/', custom_login, name='login'),
    path('onderzoek/', include('onderzoek_app.urls')),
    path('logout/', custom_logout, name='logout'),
]