Wyświetlanie wszystkich obiektów:

from lab3.models import Osoba
osoby = Osoba.objects.all()
print(osoby)

Wyświetlanie obiektu modelu Osoba z id = 3:

osoba = Osoba.objects.get(id=3)
print(osoba)

Wyświetl obiekty modelu osoba których nazwisko rozpoczyna się na t:

osoby_k = Osoba.objects.filter(nazwisko__startswith='T')
print(osoby_k)

Wyświetl unikalną listę stanowisk przypisanych dla modeli:

stanowiska = Osoba.objects.values_list('stanowisko__nazwa', flat=True).distinct()
print(stanowiska)

Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco:

stanowiska_sorted = Osoba.objects.values_list('stanowisko__nazwa', flat=True).distinct().order_by('-stanowisko__nazwa')
print(stanowiska_sorted)

Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie:

stanowisko_test = Stanowisko.objects.get(id=1)

nowa_osoba = Osoba(imie="Jan", nazwisko="Kowalski", plec=Osoba.PlecChoices.MEZCZYZNA, stanowisko=stanowisko_test)
nowa_osoba.save()

print(nowa_osoba)