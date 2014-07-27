from django.contrib import admin
from apps.volunteer import models


class VolunteersAdmin(admin.ModelAdmin):
    list_display = [ "name", "nick_name", "phone_number"]
admin.site.register(models.Volunteer, VolunteersAdmin)


class ClassesAdmin(admin.ModelAdmin):
    list_display = ["class_name", "grade"]
admin.site.register(models.Class, ClassesAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ["course_name"]
admin.site.register(models.Course, CoursesAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_name", "description"]
admin.site.register(models.School, SchoolAdmin)

class ClassBeginAdmin(admin.ModelAdmin):
    list_display = ["course_id", "class_id","volunteer_id", "status"]
admin.site.register(models.ClassBegin, ClassBeginAdmin)


class CheckInAdmin(admin.ModelAdmin):
    list_display = ["volunteer_id", "created_at"]
admin.site.register(models.CheckIn, CheckInAdmin)