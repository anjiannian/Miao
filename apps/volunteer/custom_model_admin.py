from django.contrib import admin
from django.contrib.auth.models import Permission


class CustomModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()


    def queryset(self, request):
        qs = super(CustomModelAdmin, self).queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return qs

        return qs.filter(added_by=request.user)