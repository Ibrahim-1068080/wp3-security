# Generated by Django 5.0.1 on 2024-03-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_organisatie_beschrijving_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='bijzonderheden',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='bijzonderheden_beschikbaarheid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='gebruikte_hulpmiddelen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ervaringsdeskundige',
            name='voogd',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
