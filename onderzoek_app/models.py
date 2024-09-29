from django.db import models

class Onderzoek(models.Model):
    STATUS_CHOICES = [
        ('nieuw', 'Nieuw'),
        ('goedgekeurd', 'Goedgekeurd'),
        ('afgekeurd', 'Afgekeurd'),
        ('gesloten', 'Gesloten'),
    ]
    TYPE_ONDERZOEK_CHOICES = [
        ('telefonisch', 'Telefonisch'),
        ('op_locatie', 'Op Locatie'),
        ('via_internet', 'Via Internet'),
    ]

    titel = models.CharField(max_length=200)
    beschrijving = models.TextField()
    startdatum = models.DateField()
    einddatum = models.DateField()
    criteria = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='nieuw')
    type_onderzoek = models.CharField(max_length=100, choices=TYPE_ONDERZOEK_CHOICES, default='telefonisch')
    doelgroep_leeftijd_van = models.IntegerField(null=True, blank=True)
    doelgroep_leeftijd_tot = models.IntegerField(null=True, blank=True)
    doelgroep_beperking = models.CharField(max_length=255,blank=True)
    met_beloning = models.BooleanField(default=False)
    beloning_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titel