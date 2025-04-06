from rest_framework.permissions import BasePermission
from user.models import CustomUser


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == CustomUser.Roles.OWNER)
    