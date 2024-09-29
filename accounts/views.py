from django.shortcuts import render, redirect, get_object_or_404
from .forms import ErvaringsdeskundigeForm, ErvaringsdeskundigeUpdateForm, OrganisatieForm, OrganisatieUpdateForm,OnderzoekForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse ,HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import accounts_onderzoek, get_onderzoek_lijst, Organisatie, Deelname, Onderzoek
import uuid





def ervaringsdeskundige_aanmaken_view(request):
    if request.method == 'POST':
        form = ErvaringsdeskundigeForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logout(request)
            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = ErvaringsdeskundigeForm()
        return render(request, 'accounts/register.html', {'form': form})


def organisatie_aanmaken_view(request):
    if request.method == 'POST':
        form = OrganisatieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrganisatieForm()
    return render(request, 'accounts/Organisatie/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"User {username} authenticated")
                if user.is_staff:
                    print("User is staff")
                    login(request, user)
                    return redirect('/admin/')
                elif (hasattr(user, 'organisatie') and user.organisatie.is_verified) or \
                     (hasattr(user, 'ervaringsdeskundige') and user.ervaringsdeskundige.is_verified):
                    print("User is verified")
                    login(request, user)
                    return redirect('index')
                else:
                    print("User is not verified")
                    form.add_error(None, 'Je accounts moet nog geverifieerd worden')
            else:
                print(f"Failed to authenticate user {username}")
                form.add_error(None, 'Verkeerde gebruikersnaam of wachtwoord')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def onderzoek_list(request):
    onderzoek_lijst = get_onderzoek_lijst()
    context = {'onderzoek_lijst': onderzoek_lijst}
    return render(request, 'onderzoeken.html', context)

@login_required
def ervaringsdeskundige_profiel(request):
    ervaringsdeskundige = request.user.ervaringsdeskundige
    if request.method == 'POST':
        form = ErvaringsdeskundigeUpdateForm(request.POST, instance=ervaringsdeskundige)
        if form.is_valid():
            form.save()
            return redirect('ervaringdeskundige_profiel')
    else:
        form = ErvaringsdeskundigeUpdateForm(instance=ervaringsdeskundige)
    return render(request, 'accounts/ervaringdeskundige_profiel.html', {'form': form})

@login_required
def organisatie_profiel(request):
    organisatie = request.user.organisatie
    if request.method == 'POST':
        form = OrganisatieUpdateForm(request.POST, instance=organisatie)
        if form.is_valid():
            form.save()
            return redirect('organisatie_profiel')
    else:
        form = OrganisatieUpdateForm(instance=organisatie)
    return render(request, 'accounts/Organisatie/organisatie_profiel.html', {'form': form})

@login_required
def genereer_api_key(request):
    user = request.user
    if hasattr(user, 'organisatie'):
        user.organisatie.api_key = uuid.uuid4()
        user.organisatie.save()
        message = "Niewe API key Is gegenereerd"
    else:
        message = "Je bent niet bevoegd om een API te genereren"
    return render(request, 'accounts/Organisatie/api_pagina.html', {'message': message})


@login_required
def deelnemen(request, onderzoek_id):
    onderzoek = get_object_or_404(Onderzoek, pk=onderzoek_id)

    gebruiker = request.user

    deelname, created = Deelname.objects.get_or_create(
        onderzoek=onderzoek,
        gebruiker=gebruiker,
    )

    if created:
        response_data = {"success": True}
    else:
        response_data = {"success": False, "message": "U bent al ingeschreven voor dit onderzoek."}

    return JsonResponse(response_data)


@login_required
def profile(request):
    user = request.user
    organisatie = user.organisatie
    context = {'organisatie': organisatie}
    return render(request, 'profile.html', context)
@login_required
def create_onderzoek(request):
    if request.method == 'POST':
        form = OnderzoekForm(request.POST)
        if form.is_valid():
            onderzoek = form.save()
            return redirect('create_onderzoek')
    else:
        form = OnderzoekForm()
    return render(request, 'create_onderzoek.html', {'form': form})

def about2(request):
    return render(request, 'accounts/about.html')


def deelname_lijst(request):
    deelnames = Deelname.objects.all()
    return render(request, 'deelname_lijst.html', {'deelnames': deelnames})

def verify_onderzoek(request):
    if request.method == 'POST':
        onderzoek_id = request.POST.get('onderzoek_id')
        onderzoek = get_object_or_404(Onderzoek, id=onderzoek_id)
        onderzoek.is_verified = True
        onderzoek.save()
        return redirect('verify_onderzoek')
    else:
        onderzoeken = Onderzoek.objects.filter(is_verified=False)
        return render(request, 'verify_onderzoek.html', {'onderzoeken': onderzoeken})