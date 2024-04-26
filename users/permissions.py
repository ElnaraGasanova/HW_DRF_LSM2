


class IsOwner(object):

    def has_object_permission(self, request, view, obj):
        #группа д.наз-ся
        return request.user == obj.owner


class IsModerator(object):

    def has_permission(self, request, view):
        #группа д.наз-ся moderator
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False