from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    '''Проверка принадлежности пользователя к группе "Модератор".'''
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsOwner(permissions.BasePermission):
    '''Проверяет является ли пользователь Владельцем.'''
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
