from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.conf import settings
from onderzoek_app.models import Onderzoek
import uuid


class Ervaringsdeskundige(models.Model):

    GESLACHT_CHOICES = [
        ('man', 'Man'),
        ('vrouw', 'Vrouw'),
        ('anders', 'Anders'),
    ]
    VOORKEUR_BENADERING_CHOICES = [
        ('telefonisch', 'Telefonisch'),
        ('email', 'Email'),
    ]
    TYPE_ONDERZOEK_CHOICES = [
        ('telefonisch', 'Telefonisch'),
        ('email', 'Email'),
        ('op locatie', 'Op locatie')
    ]
    TYPE_BEPERKING_CHOICES = [
        ('Geen Beperking', 'Geen Beperking'),
        ('Doof', 'Doof'),
        ('Slechthorend', 'Slechthorend'),
        ('Doofblind (Auditief)', 'Doofblind (Auditief)'),
        ('Blind', 'Blind'),
        ('Slechtziend', 'Slechtziend'),
        ('Kleurenblind', 'Kleurenblind'),
        ('DoofblindVisueel', 'Doofblind (Visueel)'),
        ('Amputatie en mismaaktheid', 'Amputatie en mismaaktheid'),
        ('Artritus', 'Artritus'),
        ('Fibromyalgie', 'Fibromyalgie'),
        ('Reuma', 'Reuma'),
        ('Verminderde handvaardigheid', 'Verminderde handvaardigheid'),
        ('Spierdystrofie', 'Spierdystrofie'),
        ('RSI', 'RSI'),
        ('Tremor en Spasmen', 'Tremor en Spasmen'),
        ('Quadriplegie of tetraplegie', 'Quadriplegie of tetraplegie'),
        ('ADHD', 'ADHD'),
        ('Autisme', 'Autisme'),
        ('Leerstoornis', 'Leerstoornis'),
        ('Geheugen beperking', 'Geheugen beperking'),
        ('Multiple Sclerose', 'Multiple Sclerose'),
        ('Epilepsie', 'Epilepsie'),
        ('Migraine', 'Migraine'),
        ]

    gebruiker = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ervaringsdeskundige')
    is_verified = models.BooleanField(default=False)
    voornaam = models.CharField(max_length=100)
    achternaam = models.CharField(max_length=100)
    postcode = models.CharField(max_length=6)
    geslacht = models.CharField(max_length=10, choices=GESLACHT_CHOICES)
    email = models.EmailField(blank=True, null=True)
    telefoonnummer = models.CharField(max_length=15)
    geboortedatum = models.DateField()
    beperkingen = models.CharField(max_length=100, choices=TYPE_BEPERKING_CHOICES, blank=True, default='Geen Beperking')
    gebruikte_hulpmiddelen = models.TextField(blank=True, null=True)
    bijzonderheden = models.TextField(blank=True, null=True)
    voogd = models.BooleanField(blank=True, null=True)
    naam_voogd = models.CharField(max_length=100, blank=True, null=True)
    email_voogd = models.EmailField(blank=True, null=True)
    telefoonnummer_voogd = models.CharField(max_length=15, blank=True, null=True)
    voorkeur_benadering = models.CharField(max_length=15, choices=VOORKEUR_BENADERING_CHOICES)
    type_onderzoek = models.CharField(max_length=15, choices=VOORKEUR_BENADERING_CHOICES)
    bijzonderheden_beschikbaarheid = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"


class Onderzoek(models.Model):
    STATUS_CHOICES = [
        ('nieuw', 'Nieuw'),
        ('goedgekeurd', 'Goedgekeurd'),
        ('afgekeurd', 'Afgekeurd'),
        ('gesloten', 'Gesloten'),
    ]
    TYPE_ONDERZOEK_CHOICES = [
        ('op_locatie', 'Op locatie'),
        ('telefonisch', 'Telefonisch'),
        ('online', 'Online'),
    ]

    titel = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='nieuw')
    is_beschikbaar = models.BooleanField(default=True)
    beschrijving = models.TextField()
    datum_vanaf = models.DateField()
    datum_tot = models.DateField()
    type_onderzoek = models.CharField(max_length=50, choices=TYPE_ONDERZOEK_CHOICES)
    locatie = models.CharField(max_length=255, blank=True, null=True)
    met_beloning = models.BooleanField(default=False)
    beloning = models.TextField(blank=True, null=True)
    doelgroep_leeftijd_van = models.IntegerField()
    doelgroep_leeftijd_tot = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.titel

from django.db import models

class Organisatie(models.Model):
    TYPE_CHOICES = [
        ('commercieel', 'Commercieel'),
        ('non_profit', 'Non-profit'),
    ]
    gebruiker = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organisatie', null=True, blank=True)
    naam = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    website = models.CharField(max_length=50)
    beschrijving = models.TextField(blank=True)
    contactpersoon = models.CharField(max_length=255)
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=15, blank=True, null=True)
    overige_details = models.TextField(blank=True, null=True)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.naam

class Beheerder(admin.ModelAdmin):
    list_display = ['naam', 'email']

class Bericht(models.Model):
    afzender = models.ForeignKey(User, related_name='verzonden_berichten', on_delete=models.CASCADE)
    ontvanger = models.ForeignKey(User, related_name='ontvangen_berichten', on_delete=models.CASCADE)
    onderwerp = models.CharField(max_length=255)
    bericht = models.TextField()
    verzenddatum = models.DateTimeField(auto_now_add=True)
    gelezen = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.onderwerp} - van {self.afzender} aan {self.ontvanger}"
    
class accounts_onderzoek(models.Model):
    titel = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    beschrijving = models.CharField(max_length=255)
    datum_vanaf = models.DateField()
    datum_tot = models.DateField()
    type_onderzoek = models.CharField(max_length=255)
    beloning = models.FloatField(default=0.0)
    leeftijd_van = models.IntegerField(null=True, blank=True)
    leeftijd_tot = models.IntegerField(null=True, blank=True)
   


def get_onderzoek_lijst():
    return Onderzoek.objects.all()

class Deelname(models.Model):
    onderzoek = models.ForeignKey(Onderzoek, on_delete=models.CASCADE)
    gebruiker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    datum_deelname = models.DateTimeField(auto_now_add=True)