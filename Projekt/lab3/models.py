from django.db import models
from datetime import datetime

from prompt_toolkit.validation import ValidationError


def contains_number(value):
    return any(char.isdigit() for char in value)


class Osoba(models.Model):

    class PlecChoices(models.IntegerChoices):
        KOBIETA = 1, 'Kobieta'
        MEZCZYZNA = 2, 'Mężczyzna'
        INNA = 3, 'Inna'

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    plec = models.IntegerField(choices=PlecChoices.choices, default=PlecChoices.MEZCZYZNA)
    stanowisko = models.ForeignKey('Stanowisko', null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def validate(self, data_dodania):
        if data_dodania > datetime.now():
            raise ValidationError('Data dodania nie może być z przyszłości')
        if contains_number(self.imie):
            raise ValidationError('Imie nie może zawierać cyfr')

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ['nazwisko']


class Stanowisko(models.Model):

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(null=True, blank=True)

    def __str__(self):
            return self.nazwa
