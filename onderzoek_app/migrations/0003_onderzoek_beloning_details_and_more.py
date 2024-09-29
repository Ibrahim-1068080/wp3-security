# Generated by Django 5.0.1 on 2024-03-11 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onderzoek_app', '0002_alter_onderzoek_beschrijving'),
    ]

    operations = [
        migrations.AddField(
            model_name='onderzoek',
            name='beloning_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='doelgroep_beperking',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='doelgroep_leeftijd_tot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='doelgroep_leeftijd_van',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='met_beloning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='status',
            field=models.CharField(choices=[('nieuw', 'Nieuw'), ('goedgekeurd', 'Goedgekeurd'), ('afgekeurd', 'Afgekeurd'), ('gesloten', 'Gesloten')], default='nieuw', max_length=100),
        ),
        migrations.AddField(
            model_name='onderzoek',
            name='type_onderzoek',
            field=models.CharField(choices=[('telefonisch', 'Telefonisch'), ('op_locatie', 'Op Locatie'), ('via_internet', 'Via Internet')], default='telefonisch', max_length=100),
        ),
        migrations.AlterField(
            model_name='onderzoek',
            name='beschrijving',
            field=models.TextField(),
        ),
    ]