from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS: #mesela http get safe methos. Cunku sadece veri okuyor
            return True

        return obj.id == request.user.id
