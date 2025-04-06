from django.db import models


class Stadium(models.Model):
    owner = models.ForeignKey('user.CustomUser', related_name='stadium_owner', on_delete=models.CASCADE, limit_choices_to={'role': 'owner'})
    name = models.CharField(max_length=225, unique=True)
    location = models.CharField(max_length=225)
    capacity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='stadiums/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.location})"


class StadiumManager(models.Model):
    stadium = models.OneToOneField('Stadium', related_name='stadium_manager', on_delete=models.CASCADE)
    manager = models.ForeignKey('user.CustomUser', related_name='managed_stadiums', on_delete=models.CASCADE, limit_choices_to={'role': 'manager'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.manager.first_name} {self.manager.last_name} - {self.stadium.name}"
