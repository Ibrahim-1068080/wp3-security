# Generated by Django 5.0.1 on 2024-03-10 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_onderzoek'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Onderzoek',
            new_name='accounts_onderzoek',
        ),
    ]
