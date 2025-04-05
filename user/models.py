from django.db import models

from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        OWNER = 'owner', 'Owner'
        MANAGER = 'manager', 'Manager'

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.email} - {self.role}"
