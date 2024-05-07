from django.contrib import admin
from .models import Service, Type
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'price',
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Type, TypeAdmin)
