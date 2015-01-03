from django.contrib import admin
from django.contrib.auth.models import Permission


class CustomModelAdmin(admin.ModelAdmin):
   
    def has_view_permission(self, request, obj=None):
        opts = self.opts
        view_permission = 'view_%s' %self.model._meta.module_name
        return request.user.has_perm(opts.app_label + '.' + view_permission)
   
    def has_change_permission(self, request, obj=None):
        if hasattr(self,'has_change'):
            if self.has_change:
                return True
       
        return super(CustomModelAdmin,self).has_change_permission(request, obj)
       
    def get_model_perms(self, request):
        value = super(CustomModelAdmin,self).get_model_perms(request)
        value['view'] = self.has_view_permission(request)
        return value
   
    def changelist_view(self, request, extra_context=None):
        if self.has_view_permission(request, None):
            self.has_change = True
        result = super(CustomModelAdmin,self).changelist_view(request, extra_context)
        self.has_change = False
        return result 