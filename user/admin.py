from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


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
        'phone_number',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
        'role',
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
            'fields': ('email', 'password1', 'password2',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'role',),
        }),
    )
