from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomAdminData(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Gebruiker(models.Model):
    naam = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    actief = models.BooleanField(default=True)

    def __str__(self):
        return self.naam

onderzoeker = models.BooleanField(default=False)

print('h')

def __str__(self):
    return self.titel