from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    fields = ['ci', 'email', 'name', 'lastname', 'birthdate']


admin.site.register(Person, PersonAdmin)
