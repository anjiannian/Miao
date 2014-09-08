from django.contrib import admin
from apps.volunteer import models


class VolunteersAdmin(admin.ModelAdmin):
    list_display = ["name", "nick_name", "phone_number"]


admin.site.register(models.Volunteer, VolunteersAdmin)


class ClassesAdmin(admin.ModelAdmin):
    list_display = ["class_name", "grade"]


admin.site.register(models.Class, ClassesAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(models.Course, CoursesAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_name", "description"]


admin.site.register(models.School, SchoolAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["course", "class_id", "activity_type", "status"]


admin.site.register(models.Activity, ActivityAdmin)


class CheckInAdmin(admin.ModelAdmin):
    list_display = ["volunteer", "created_at"]


admin.site.register(models.CheckIn, CheckInAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "auth", "description"]


admin.site.register(models.Book, BookAdmin)


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ["evaluation_value"]


admin.site.register(models.Evaluation, EvaluationAdmin)


class EvaluationRuleAdmin(admin.ModelAdmin):
    list_display = ["item"]


admin.site.register(models.EvaluationRule, EvaluationRuleAdmin)