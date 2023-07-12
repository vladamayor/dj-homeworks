from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_superuser:
            return True
        elif request.method == 'PUTCH' or 'DELETE':
            return request.user == obj.creator

