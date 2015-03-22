from django.contrib import admin
from django.contrib.admin.util import flatten_fieldsets


class CustomModelAdmin(admin.ModelAdmin):
    def _get_all_fields(self, exclude_list=None):
        if self.declared_fieldsets:
            result = flatten_fieldsets(self.declared_fieldsets)
        else:
            result = list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))
        return [field for field in result if field not in exclude_list]

    @staticmethod
    def has_view_permission(request, codename):
        return request.user.has_perm("%s.%s" % ('volunteer', codename))
