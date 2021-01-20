from django.contrib import admin

from .models import ClientTour


@admin.register(ClientTour)
class ClientTourAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = [
        'id',
        'client_kakaotalk_id',
        'tour_streaming_date_kst',
        'tour_streaming_link'
    ]
    search_fields = [
        'id',
    ]

    def client_kakaotalk_id(self, obj):
        return obj.client.kakaotalk_id

    def tour_streaming_date_kst(self, obj):
        return obj.tour.streaming_date

    def tour_streaming_link(self, obj):
        return obj.tour.streaming_link
