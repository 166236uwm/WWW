import pytest
from django.db.utils import IntegrityError
from Projekt.lab3.models import Osoba, Stanowisko

@pytest.mark.django_db
def test_create_stanowisko():
    stanowisko = Stanowisko.objects.create(nazwa="Developer", opis="Writes code")
    assert stanowisko.nazwa == "Developer"
    assert stanowisko.opis == "Writes code"

@pytest.mark.django_db
def test_create_osoba():
    stanowisko = Stanowisko.objects.create(nazwa="Manager", opis="Manages team")
    osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec=Osoba.PlecChoices.MEZCZYZNA, stanowisko=stanowisko)
    assert osoba.imie == "Jan"
    assert osoba.nazwisko == "Kowalski"
    assert osoba.plec == Osoba.PlecChoices.MEZCZYZNA
    assert osoba.stanowisko == stanowisko

@pytest.mark.django_db
def test_osoba_str():
    osoba = Osoba.objects.create(imie="Anna", nazwisko="Nowak", plec=Osoba.PlecChoices.KOBIETA)
    assert str(osoba) == "Anna Nowak"

@pytest.mark.django_db
def test_stanowisko_str():
    stanowisko = Stanowisko.objects.create(nazwa="Tester", opis="Tests code")
    assert str(stanowisko) == "Tester"

@pytest.mark.django_db
def test_osoba_ordering():
    osoba1 = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec=Osoba.PlecChoices.MEZCZYZNA)
    osoba2 = Osoba.objects.create(imie="Anna", nazwisko="Nowak", plec=Osoba.PlecChoices.KOBIETA)
    osoby = Osoba.objects.all()
    assert list(osoby) == [osoba1, osoba2]