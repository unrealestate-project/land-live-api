from django.contrib import admin

from .models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
        'real_estate',
        'streaming_date',
        'streaming_duration_min',
        'streaming_link',
        'min_book_client',
    ]
    search_fields = [
        'id',
        'streaming_date',
        'streaming_link',
    ]
