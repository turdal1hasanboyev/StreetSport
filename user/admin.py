from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "StreetSport Admin Panel"
admin.site.site_title = "StreetSport Admin Panel"
admin.site.index_title = "Welcome to StreetSport Admin Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'role',
        'phone_number',
        'image',
        'is_superuser',
        'is_staff',
        'is_active',
        'last_login',
        'date_joined',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'role',
        'phone_number',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
        'role',
        'date_joined',
    )
    readonly_fields = (
        'id',
        'date_joined',
        'last_login',
    )
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password',),
        }),
        ("Personal Info", {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'image', 'phone_number', 'description',),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_superuser', 'is_staff', 'is_active', 'role',),
        }),
        ("Important Dates", {
            'classes': ('wide',),
            'fields': ('date_joined', 'last_login',),
        }),
        ("ID", {
            'classes': ('wide',),
            'fields': ('id',),
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
        ("Permissions", {
            'classes': ('wide',),
            'fields': ('is_superuser', 'is_staff', 'is_active', 'role',),
        }),
    )
