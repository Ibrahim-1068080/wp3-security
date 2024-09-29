# Generated by Django 4.2.10 on 2024-02-12 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Beperking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("naam", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Organisatie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("naam", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("commercieel", "Commercieel"),
                            ("non_profit", "Non-profit"),
                        ],
                        max_length=50,
                    ),
                ),
                ("website", models.URLField(blank=True, null=True)),
                ("beschrijving", models.TextField(blank=True, null=True)),
                ("contactpersoon", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "telefoonnummer",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("overige_details", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Onderzoek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titel", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("nieuw", "Nieuw"),
                            ("goedgekeurd", "Goedgekeurd"),
                            ("afgekeurd", "Afgekeurd"),
                            ("gesloten", "Gesloten"),
                        ],
                        default="nieuw",
                        max_length=50,
                    ),
                ),
                ("is_beschikbaar", models.BooleanField(default=True)),
                ("beschrijving", models.TextField()),
                ("datum_vanaf", models.DateField()),
                ("datum_tot", models.DateField()),
                (
                    "type_onderzoek",
                    models.CharField(
                        choices=[
                            ("op_locatie", "Op locatie"),
                            ("telefonisch", "Telefonisch"),
                            ("online", "Online"),
                        ],
                        max_length=50,
                    ),
                ),
                ("locatie", models.CharField(blank=True, max_length=255, null=True)),
                ("met_beloning", models.BooleanField(default=False)),
                ("beloning", models.TextField(blank=True, null=True)),
                ("doelgroep_leeftijd_van", models.IntegerField()),
                ("doelgroep_leeftijd_tot", models.IntegerField()),
                (
                    "doelgroep_beperking",
                    models.ManyToManyField(to="accounts.beperking"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ervaringsdeskundige",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("voornaam", models.CharField(max_length=100)),
                ("achternaam", models.CharField(max_length=100)),
                ("postcode", models.CharField(max_length=6)),
                (
                    "geslacht",
                    models.CharField(
                        choices=[
                            ("man", "Man"),
                            ("vrouw", "Vrouw"),
                            ("anders", "Anders"),
                        ],
                        max_length=10,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("telefoonnummer", models.CharField(max_length=15)),
                ("geboortedatum", models.DateField()),
                ("gebruikte_hulpmiddelen", models.TextField(blank=True)),
                ("bijzonderheden", models.TextField(blank=True)),
                ("voogd", models.BooleanField(default=False)),
                ("naam_voogd", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "email_voogd",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "telefoonnummer_voogd",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "voorkeur_benadering",
                    models.CharField(
                        choices=[("telefonisch", "Telefonisch"), ("email", "Email")],
                        max_length=15,
                    ),
                ),
                (
                    "type_onderzoek",
                    models.CharField(
                        choices=[
                            ("telefonisch", "Telefonisch"),
                            ("internet", "Internet"),
                            ("op_locatie", "Op locatie"),
                        ],
                        max_length=15,
                    ),
                ),
                ("bijzonderheden_beschikbaarheid", models.TextField(blank=True)),
                ("beperkingen", models.ManyToManyField(to="accounts.beperking")),
                (
                    "gebruiker",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ervaringsdeskundige",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]