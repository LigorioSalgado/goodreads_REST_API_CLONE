from rest_framework import permissions

class EdwinPermmission(permissions.BasePermission):
    message = "No eres Edwin"

    def has_permission(self,request,view):

        if request.method == "GET" and request.user.email  == "lesf@gmail.com":
            return True
        else:
            return False
