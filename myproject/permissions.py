from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    
   # Admin kullanıcılar için tam izinler sağlar, diğerleri için sadece okuma izni sağlar.
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAdminUser(permissions.BasePermission):
    
    #Yalnızca admin kullanıcılar için tam izinler sağlar.
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    


    