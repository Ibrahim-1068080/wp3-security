from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onderzoek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=200)),
                ('beschrijving', models.TextField()),
                ('startdatum', models.DateField()),
                ('einddatum', models.DateField()),
                ('criteria', models.TextField()),
            ],
        ),
    ]
