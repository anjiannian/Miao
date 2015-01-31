from django.contrib import admin
from django.contrib.auth.models import Permission

from models import Volunteer


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

        vol_info = Volunteer.objects.get(user_id=request.user.id)
        if vol_info.level == '02':   # group leader
            pass
        elif vol_info.level == '03':  # group master
            pass
        return qs.filter(id=1)