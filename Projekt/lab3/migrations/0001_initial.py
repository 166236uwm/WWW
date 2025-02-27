# Generated by Django 4.2.16 on 2024-10-17 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=60)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.CharField(choices=[('K', 'Kobieta'), ('M', 'Mężczyzna'), ('I', 'Inna')], default='M', max_length=1)),
                ('stanowisko', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab3.stanowisko')),
            ],
        ),
    ]
