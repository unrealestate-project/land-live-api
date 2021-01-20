from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
        'kakaotalk_id',
    ]
    search_fields = [
        'id',
        'kakaotalk_id',
    ]
