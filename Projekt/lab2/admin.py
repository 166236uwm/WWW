from django.contrib import admin

# Register your models here.
from .models import Team, Person, Car

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Car)


