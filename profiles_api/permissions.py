from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile only"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""

        # if the request is a safe method, like GET or HEAD,allow
        if request.method in permissions.SAFE_METHODS:
            return True
        # else we see if the user is trying to edit their own profile
        # by comparing the user's id with the user id being requested
        return obj.id == request.user.id
