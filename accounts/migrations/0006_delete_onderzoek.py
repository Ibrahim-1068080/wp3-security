# Generated by Django 4.2.10 on 2024-03-09 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_ervaringsdeskundige_bijzonderheden_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Onderzoek",),
    ]
