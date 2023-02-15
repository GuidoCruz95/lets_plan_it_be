from django.contrib import admin
from .models import Person, Cell, Macro


class MacroAdmin(admin.ModelAdmin):
    fields = ['name', 'creation_date', 'closing_date']


class CellAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'macro']


class PersonAdmin(admin.ModelAdmin):
    fields = ['ci', 'email', 'name', 'lastname', 'birthdate', 'cell']


admin.site.register(Macro, MacroAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Person, PersonAdmin)
