from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    ordering = ('-id',)
    list_display = (
        'id',
        'user',
        'stadium',
        'start_time',
        'end_time',
        'status',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'user__email',
        'stadium__name',
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id',
    )
