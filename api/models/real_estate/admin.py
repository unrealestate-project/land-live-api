from django.contrib import admin

from .models import RealEstate


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
        'broker',
        'zigbang_link',
        'dabang_link',
        'naver_estate_link',
        'peterpan_link',
    ]
    search_fields = [
        'id',
        'broker',
    ]
