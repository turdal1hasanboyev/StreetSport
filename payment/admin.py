from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    ordering = ('id',)
    list_display = (
        'id',
        'booking',
        # 'amont',
        'status',
        'payment_method',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'status',
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id',
    )
