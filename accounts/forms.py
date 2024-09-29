from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ervaringsdeskundige, Onderzoek, Organisatie
from django.forms import ModelForm


class ErvaringsdeskundigeForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Gebruikersnaam')
    email = forms.EmailField(label='E-mailadres')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Wachtwoord')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Bevestig Wachtwoord')
    voornaam = forms.CharField(max_length=100, label='Voornaam')
    achternaam = forms.CharField(max_length=100, label='Achternaam')
    postcode = forms.CharField(max_length=6, label='Postcode')
    geslacht = forms.ChoiceField(choices=Ervaringsdeskundige.GESLACHT_CHOICES, label='Geslacht')
    telefoonnummer = forms.CharField(max_length=15, label='Telefoonnummer')
    geboortedatum = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Geboortedatum')
    beperkingen = forms.ChoiceField(choices=Ervaringsdeskundige.TYPE_BEPERKING_CHOICES, required=False, label='Beperking')
    gebruikte_hulpmiddelen = forms.CharField(widget=forms.Textarea, required=False, label='Gebruikte hulpmiddelen')
    bijzonderheden = forms.CharField(widget=forms.Textarea, required=False, label='Bijzonderheden')
    voogd = forms.BooleanField(required=False, label='Voogd')
    naam_voogd = forms.CharField(max_length=100, required=False, label='Naam Voogd')
    email_voogd = forms.EmailField(required=False, label='E-mailadres Voogd')
    telefoonnummer_voogd = forms.CharField(max_length=15, required=False, label='Telefoonnummer Voogd')
    voorkeur_benadering = forms.ChoiceField(choices=Ervaringsdeskundige.VOORKEUR_BENADERING_CHOICES,
                                            label='Voorkeur Benadering')
    type_onderzoek = forms.ChoiceField(choices=Ervaringsdeskundige.TYPE_ONDERZOEK_CHOICES, label='Type Onderzoek')
    bijzonderheden_beschikbaarheid = forms.CharField(widget=forms.Textarea, required=False,
                                                     label='Bijzonderheden Beschikbaarheid')

    class Meta:
        model = Ervaringsdeskundige
        fields = ['username', 'email', 'password1', 'password2', 'voornaam', 'achternaam', 'postcode', 'geslacht',
                  'telefoonnummer', 'geboortedatum', 'beperkingen', 'gebruikte_hulpmiddelen', 'bijzonderheden', 'voogd',
                  'naam_voogd', 'email_voogd', 'telefoonnummer_voogd', 'voorkeur_benadering', 'type_onderzoek',
                  'bijzonderheden_beschikbaarheid']
        exclude = ['gebruiker', 'is_verified']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Wachtwoorden komen niet overeen")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Deze gebruikersnaam is al in gebruik")
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        ervaringsdeskundige = super().save(commit=False)
        ervaringsdeskundige.gebruiker = user
        if commit:
            ervaringsdeskundige.save()
            self._save_m2m()
        return ervaringsdeskundige

class ErvaringsdeskundigeUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='E-mailadres')

    class Meta:
        model = Ervaringsdeskundige
        fields = ['voornaam', 'achternaam', 'postcode', 'geslacht', 'telefoonnummer', 'geboortedatum', 'beperkingen',
                  'gebruikte_hulpmiddelen', 'bijzonderheden', 'voogd', 'naam_voogd', 'email_voogd',
                  'telefoonnummer_voogd', 'voorkeur_benadering', 'type_onderzoek', 'bijzonderheden_beschikbaarheid']

    def __init__(self, *args, **kwargs):
        super(ErvaringsdeskundigeUpdateForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.gebruiker:
            self.fields['email'].initial = self.instance.gebruiker.email

    def save(self, commit=True):
        ervaringsdeskundige = super().save(commit=False)
        if commit:
            ervaringsdeskundige.gebruiker.email = self.cleaned_data['email']
            ervaringsdeskundige.gebruiker.save()
            ervaringsdeskundige.save()
        return ervaringsdeskundige

class OrganisatieForm(UserCreationForm):
    naam = forms.CharField(max_length=255, label='Naam van de organisatie')
    type = forms.ChoiceField(choices=Organisatie.TYPE_CHOICES, label='Type')
    website = forms.CharField(max_length=255, label='website', required=False)
    beschrijving = forms.CharField(widget=forms.Textarea, required=False, label='Beschrijving')
    contactpersoon = forms.CharField(max_length=255, label='Contactpersoon')
    email = forms.EmailField(label='E-mailadres voor de organisatie')
    telefoonnummer = forms.CharField(max_length=15, required=False, label='Telefoonnummer')
    overige_details = forms.CharField(widget=forms.Textarea, required=False, label='Overige details')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            organisatie = Organisatie.objects.create(
                gebruiker=user,
                naam=self.cleaned_data['naam'],
                type=self.cleaned_data['type'],
                website=self.cleaned_data['website'],
                beschrijving=self.cleaned_data['beschrijving'],
                contactpersoon=self.cleaned_data['contactpersoon'],
                email=self.cleaned_data['email'],
                telefoonnummer=self.cleaned_data['telefoonnummer'],
                overige_details=self.cleaned_data['overige_details']
            )
        return user

class OrganisatieUpdateForm(forms.ModelForm):
    class Meta:
        model = Organisatie
        fields = ['naam', 'type', 'website', 'beschrijving', 'contactpersoon', 'email', 'telefoonnummer', 'overige_details']

class OnderzoekForm(forms.ModelForm):
    class Meta:
        model = Onderzoek
        fields = ['titel', 'status', 'is_beschikbaar', 'beschrijving', 'datum_vanaf', 'datum_tot', 'type_onderzoek', 'locatie', 'met_beloning', 'beloning', 'doelgroep_leeftijd_van', 'doelgroep_leeftijd_tot']

