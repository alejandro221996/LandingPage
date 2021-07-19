from django.contrib import admin

from .models import services

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'created')


admin.site.register(services, ServiceAdmin)
