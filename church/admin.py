from django.contrib import admin
from .models import Person, Cell, Macro, Subscription


class MacroAdmin(admin.ModelAdmin):
    fields = ['name', 'creation_date', 'closing_date']


class CellAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'macro']


class PersonAdmin(admin.ModelAdmin):
    fields = ['ci', 'email', 'name', 'lastname', 'birthdate', 'cell']


class SubscriptionAdmin(admin.ModelAdmin):
    fields = ['subscription_id', 'person', 'event', 'payment_status', 'notes']


admin.site.register(Macro, MacroAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
