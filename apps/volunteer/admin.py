#-*- coding: UTF-8 -*-
from django.contrib import admin

from custom_model_admin import CustomModelAdmin
from apps.volunteer import models


class VolunteersAdmin(CustomModelAdmin):
    def queryset(self, request):
        qs = super(CustomModelAdmin, self).queryset(request)

        # If super-user, show all
        if request.user.is_superuser:
            return qs

        filter_dict = {}
        vol_info = models.Volunteer.objects.get(user_id=request.user.id)
        if vol_info.level == '02':   # group leader
            pass
        elif vol_info.level == '03':  # group master
            # filter_dict[]
            pass
        return qs.filter(filter_dict)

    readonly_fields = ("level", )
    list_display = ["name", "nick_name", "phone_number", "created_at", "status"]
admin.site.register(models.Volunteer, VolunteersAdmin)


class VolunteerGroupAdmin(CustomModelAdmin):
    def queryset(self, request):
        qs = super(CustomModelAdmin, self).queryset(request)

        return qs.filter(status=0)   # omit all obsolete data
    list_display = ["group_name",]
admin.site.register(models.VolunteerGroup, VolunteerGroupAdmin)


class ClassesAdmin(CustomModelAdmin):
    list_display = ["class_name", "grade"]
admin.site.register(models.Class, ClassesAdmin)


class CoursesAdmin(CustomModelAdmin):
    list_display = ["name"]
admin.site.register(models.Course, CoursesAdmin)


class SchoolAdmin(CustomModelAdmin):
    list_display = ["school_name", "description"]
admin.site.register(models.School, SchoolAdmin)


class ActivityAdmin(CustomModelAdmin):
    list_display = ["activity_name", "course", "class_id", "activity_type", "status"]
admin.site.register(models.Activity, ActivityAdmin)


class CheckInAdmin(CustomModelAdmin):
    list_display = ["volunteer", "created_at"]
admin.site.register(models.CheckIn, CheckInAdmin)


class BookAdmin(CustomModelAdmin):
    list_display = ["owner_school", "name", "auth", "description"]
admin.site.register(models.Book, BookAdmin)


class EvaluationAdmin(CustomModelAdmin):
    list_display = ["evaluation_value"]
admin.site.register(models.Evaluation, EvaluationAdmin)


class EvaluationRuleAdmin(CustomModelAdmin):
    list_display = ["item"]
admin.site.register(models.EvaluationRule, EvaluationRuleAdmin)
