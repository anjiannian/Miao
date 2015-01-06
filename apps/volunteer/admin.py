#-*- coding: UTF-8 -*-
from django.contrib import admin

from custom_model_admin import CustomModelAdmin
from apps.volunteer import models


class VolunteersAdmin(CustomModelAdmin):
    list_display = ["name", "nick_name", "phone_number", "status"]


admin.site.register(models.Volunteer, VolunteersAdmin)


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
    list_display = ["course", "class_id", "activity_type", "status"]


admin.site.register(models.Activity, ActivityAdmin)


class CheckInAdmin(CustomModelAdmin):
    list_display = ["volunteer", "created_at"]


admin.site.register(models.CheckIn, CheckInAdmin)


class BookAdmin(CustomModelAdmin):
    list_display = ["name", "auth", "description"]


admin.site.register(models.Book, BookAdmin)


class EvaluationAdmin(CustomModelAdmin):
    list_display = ["evaluation_value"]


admin.site.register(models.Evaluation, EvaluationAdmin)


class EvaluationRuleAdmin(CustomModelAdmin):
    list_display = ["item"]


admin.site.register(models.EvaluationRule, EvaluationRuleAdmin)