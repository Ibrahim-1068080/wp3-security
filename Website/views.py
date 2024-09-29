from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from website.models import CustomAdminData
from django.contrib.auth import logout


def home_view(request):
    return render(request, 'home.html')
def index(request):
    return render (request, 'home.html', )
def about(request):
    return render(request, 'website/about.html')

def test(request):
    return HttpResponse('<h1> test </h1>')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def home(request):
    context = {
        'user_is_admin': request.user.is_superussser,
    }
    return render(request, 'home.html', context)

def custom_logout(request):
    logout(request)
    return redirect('home')