from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles=None):
    """Decorator to enforce role-based access."""
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Allow SuperAdmins unconditionally
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # Check if user's role is in allowed_roles
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)

            # Deny access if role is not allowed
            return HttpResponseForbidden("You are not authorized to view this page.")
        return _wrapped_view
    return decorator
