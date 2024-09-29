"""
URL configuration for project_wp3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
"""

from django.contrib import admin
from django.urls import path, include
from website import views
from website.views import custom_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
import accounts.views as acc


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', acc.custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('', views.index, name='index'),
    path('about/', views.about, name='About'),
    path('test/', views.test, name='test'),
    path('', include('onderzoek_app.urls')),
    path('', include('feedback.urls')),
    path('deelnames/', acc.deelname_lijst, name='deelname'),
    path('accounts/onderzoeken/verify_onderzoek.html', acc.verify_onderzoek, name='verify_onderzoek'),
    ]