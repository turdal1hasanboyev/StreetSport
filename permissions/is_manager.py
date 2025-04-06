from rest_framework.permissions import BasePermission
from apps.user.models import CustomUser


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == CustomUser.Roles.MANAGER)
    