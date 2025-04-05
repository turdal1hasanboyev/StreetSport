from django.contrib import admin

from .models import Stadium, StadiumManager


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    model = Stadium
    ordering = ('-id',)
    list_display = (
        'id',
        'owner',
        'name',
        'location',
        'capacity',
        'price',
        'is_available',
        'image',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'owner__email',
        'name',
        'location',
    )
    list_filter = (
        'is_available',
    )
    readonly_fields = (
        'id',
    )


@admin.register(StadiumManager)
class StadiumManagerAdmin(admin.ModelAdmin):
    model = StadiumManager
    ordering = ('id',)
    list_display = (
        'id',
        'stadium',
        'manager',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'manager__email',
        'stadium__name',
    )
    readonly_fields = (
        'id',
    )
