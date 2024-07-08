from django.core.exceptions import PermissionDenied

def check_if(user):
    if not user.is_authenticated or user.username != 'ronal':
        raise PermissionDenied
