from rest_framework import permissions

from users.models import User


class SelectionPermission(permissions.BasePermission):
    message = 'У вас нет прав на редактирование'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class AdPermission(permissions.BasePermission):
    message = 'У вас нет прав на редактирование'

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return bool(request.user == obj.author or request.user.role in [User.ADMIN, User.MODERATOR])




