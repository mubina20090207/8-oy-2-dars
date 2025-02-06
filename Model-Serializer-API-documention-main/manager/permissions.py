from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffModelPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            model_meta = view.queryset.model._meta
            app_label = model_meta.app_label
            model_name = model_meta.model_name

            permissions_map = {
                "GET": f"{app_label}.view_{model_name}",
                "POST": f"{app_label}.add_{model_name}",
                "PUT": f"{app_label}.change_{model_name}",
                "PATCH": f"{app_label}.change_{model_name}",
                "DELETE": f"{app_label}.delete_{model_name}",
            }

            required_permission = permissions_map.get(request.method)

            return required_permission and request.user.has_perm(required_permission)

        return request.method in SAFE_METHODS
