from django.contrib import admin

from .models import Broker


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
        'kakaotalk_id',
        'name',
        'office_name',
        'office_address',
    ]
    search_fields = [
        'id',
        'kakaotalk_id',
        'name',
    ]
