class IsModerator(object):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsOwner(object):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
