from django.contrib import admin
from .models import Osoba, Stanowisko


class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_with_id', 'data_dodania']
    list_filter = ['data_dodania', 'stanowisko']

    @admin.display(description='Stanowisko (ID)')
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f"{obj.stanowisko} ({obj.stanowisko.id})"
        return '-'

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    slist_filter = ['nazwa']


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)


