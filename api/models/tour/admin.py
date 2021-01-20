from django.contrib import admin

from .models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
    ]
    search_fields = [
        'id',
    ]
