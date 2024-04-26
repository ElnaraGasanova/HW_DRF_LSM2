


# class IsOwner(object):
#
#     def has_object_permission(self, request, view, obj):
#         #группа д.наз-ся
#         return request.user == obj.owner


class IsModerator(object):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False
