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
            group_members = models.VolunteerGroup.objects.filter(
                group_leader_id=vol_info.id,
                status=1
            )[0]

            filter_dict["id__in"] = [v.id for v in group_members.volunteers.all()]
        elif vol_info.level == '03':  # group master
            # filter_dict[]
            self.readonly_fields = ("phone_number", "level")
            self.list_display.remove("level")
        return qs.filter(**filter_dict)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if not request.user.is_superuser:
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '01':   # normal volunteer
                pass
            elif vol_info.level == '02':   # group leader
                readonly_fields = self._get_all_fields(exclude_list=["status"])
            elif vol_info.level == '03':  # group master
                readonly_fields = ("level",)
        return readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '01':   # normal volunteer
                pass
            elif vol_info.level == '02':   # group leader
                self.exclude = ("level", "volunteer_type", "evaluation",
                                "evaluate_time", "training_time", "evaluation_of_training",
                                "homework", "free_time", )
            elif vol_info.level == '03':  # group master
                self.readonly_fields = ("level",)
                # filter_dict[]
        return super(VolunteersAdmin, self).get_form(request, obj=None, **kwargs)

    list_display = ["name", "nick_name", "phone_number", "created_at", "status"]
admin.site.register(models.Volunteer, VolunteersAdmin)


class VolunteerGroupAdmin(CustomModelAdmin):
    # def queryset(self, request):
    #     qs = super(CustomModelAdmin, self).queryset(request)
    #
    #     return qs.filter(status=0)   # omit all obsolete data
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
