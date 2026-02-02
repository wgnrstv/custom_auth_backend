from rest_framework import permissions
from .models import AccessRule

class HasResourcePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        resource_name = getattr(view, 'required_resource', None)
        required_permission = getattr(view, 'required_permission', 'view')

        if not resource_name:
            return True

        user_roles = request.user.roles.all()
        return AccessRule.objects.filter(
            role__in=user_roles,
            resource__name=resource_name,
            permission=required_permission
        ).exists()
