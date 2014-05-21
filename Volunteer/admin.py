from django.contrib import admin
from Volunteer import models

class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Volunteers, DocumentAdmin)
admin.site.register(models.Classes, DocumentAdmin)
admin.site.register(models.Courses, DocumentAdmin)
admin.site.register(models.ClassBegin, DocumentAdmin)

