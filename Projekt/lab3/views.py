from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from Projekt.lab3.models import Osoba


def osoba_view(request, pk):
    if not request.user.has_perm('lab3.view_osoba'):
        raise PermissionDenied
    try:
        person = Osoba.objects.get(pk=pk)
        return HttpResponse(f"Person: {person.name}")
    except Osoba.DoesNotExist:
        return HttpResponse("Person not found")

def other_osoba_view(request, pk):
    if not request.user.has_perm('lab3.can_view_other_persons'):
        raise PermissionDenied
    try:
        osoba = Osoba.objects.get(pk=pk)
        return HttpResponse(f"Osoba: {osoba.imie}")
    except Osoba.DoesNotExist:
        return HttpResponse("Osoba nie znaleziona")