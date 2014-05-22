from django.contrib import admin
from apps.volunteer import models


class VolunteersAdmin(admin.ModelAdmin):
    list_display = ["account", "name", "nick_name", "phone_number"]
admin.site.register(models.Volunteers, VolunteersAdmin)


class ClassesAdmin(admin.ModelAdmin):
    list_display = ["class_name", "grade"]
admin.site.register(models.Classes, ClassesAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ["course_name"]
admin.site.register(models.Courses, CoursesAdmin)


class ClassBeginAdmin(admin.ModelAdmin):
    list_display = ["course_id", "class_id","volunteer_id", ]
admin.site.register(models.ClassBegin, ClassBeginAdmin)

