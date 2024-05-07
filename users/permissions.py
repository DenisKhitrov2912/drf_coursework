from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    """Пермишен на собственника объекта"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUserUser(BasePermission):
    """Пермишен на редактирование своего профиля"""
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
