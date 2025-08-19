from rest_framework import permissions

class RolePermission(permissions.BasePermission):
    """
    Custom permission based on the user's role: Owner, Manager, Staff
    """

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated or not hasattr(user, 'role'):
            return False

        role_name = user.role.role_name.lower()
        model_name = view.basename.lower()  # comes from router registration

        # Owner: full access
        if role_name == "owner":
            return True

        # Manager: GET all, POST/PUT on most tables, restricted on Users, Roles, Theaters
        if role_name == "manager":
            if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
                if model_name in ["user", "role", "theater"]:
                    return False
                return True
            if request.method in ["POST", "PUT"]:
                if model_name in ["user", "role", "theater"]:
                    return False
                return True
            return False  # DELETE not allowed

        # Staff: GET only (cannot access Users, Roles, Theaters); POST allowed only for Tickets/Reviews
        if role_name == "staff":
            if request.method in permissions.SAFE_METHODS:
                if model_name in ["user", "role", "theater"]:
                    return False
                return True
            if request.method == "POST" and model_name in ["ticket", "review"]:
                return True
            return False  # PUT/DELETE not allowed

        # Default: deny access
        return False
