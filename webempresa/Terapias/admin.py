from django.contrib import admin
from .models import Terapias
# Register your models here.


class TerapiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'lastname', 'created', 'name_completed')
    ordering = ['lastname', 'name']
    search_fields = ['name']
    list_filter = ['name']

    def name_completed(self, obj):
        return ","


admin.site.register(Terapias, TerapiaAdmin)
