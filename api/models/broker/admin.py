from django.contrib import admin

from .models import Broker


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
    ]
    search_fields = [
        'id',
    ]
