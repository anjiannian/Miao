#-*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from custom_model_admin import CustomModelAdmin
from apps.volunteer import models
import db_utils


# ==================================================================
# =======================auth admin=================================
class SelfUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
        if not obj:
            return self.add_fieldsets
        if not request.user.is_superuser:
            fieldsets = (
                    (None, {'fields': ('username', 'password')}),
                    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                )
        return fieldsets

    def get_queryset(self, request):
        qs = super(SelfUserAdmin, self).get_queryset(request)

        # only sys_admin and operator can edit auth's user info
        # If super-user, show all
        if request.user.is_superuser:
            return qs
        else:  # only operator
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '03':
                region_records = vol_info.operator_region.all()
                schools = []
                for r in region_records:
                    for s in r.schools.all():
                        schools.append(s.id)
                volunteer_groups = models.VolunteerGroup.objects.filter(school_for_work__in=schools)
                all_user_in_region = []
                for g in volunteer_groups:
                    for v in g.volunteers.all():
                        all_user_in_region.append(v.user.id)

                return qs.filter(id__in=all_user_in_region)
            else:
                return None

    # def get_form(self, request, obj=None, **kwargs):
    #     # if not request.user.is_superuser:
    #     #     return None
    #     return super(SelfUserAdmin, self).get_form(request, obj=None, **kwargs)
admin.site.unregister(User)
admin.site.register(User, SelfUserAdmin)

# ==================================================================
# =======================self admin=================================
class VolunteersAdmin(CustomModelAdmin):

    def get_queryset(self, request):
        qs = super(CustomModelAdmin, self).get_queryset(request)

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

            return group_members.volunteers
        elif vol_info.level == '03':
            # operator 所有未审核的 和 自己所管辖下的所有志愿者
            un_evaluate_vol = models.Volunteer.objects.filter(status='10')
            evaluated_vol = db_utils.get_operators_vols(vol_info.id)
            return un_evaluate_vol | evaluated_vol

        return qs

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(VolunteersAdmin, self).get_form(request, obj=None, **kwargs)
    #
    #     if not request.user.is_superuser:
    #         vol_info = models.Volunteer.objects.get(user_id=request.user.id)
    #         if vol_info.level == '01':   # normal volunteer
    #             pass
    #         elif vol_info.level == '02':   # group leader
    #             self.exclude = ("level", "volunteer_type", "evaluation",
    #                             "evaluate_time", "training_time", "evaluation_of_training",
    #                             "homework", "free_time", )
    #         elif vol_info.level == '03':  # group master
    #             # self.readonly_fields = ("level",)
    #             pass
    #     return form

    fieldsets = (
        (u'名称', {
            'fields': ('name', 'phone_number')
        }),
        (u"基本信息", {
            'fields': ('nick_name', 'en_name', 'sex', 'age',
                       'wei_xin', 'weibo', 'is_in_school', 'graduated_school',
                       'education_background', 'profession', 'grade', 'forte',
                       'recent_company', 'job', 'working_years'),
            'classes': ('collapse ',)
        }),
        (u'志愿者申请信息', {
            'fields': ('why_in', 'want_to', 'self_introduction', 'volunteer_experience',
                       'reference', 'headshot'),
            'classes': ('collapse ',)
        }),
        (u'审核信息', {
            'fields': ('evaluation', 'evaluate_time'),
            'classes': ('collapse ',)
        }),
        (u'培训信息', {
            'fields': ('training_time', 'evaluation_of_training', 'homework'),
            'classes': ('collapse ',)
        }),
        (None, {
            'fields': ('status', )
        })
    )
    def get_fieldsets(self, request, obj=None):
        fieldsets = self.fieldsets
        if not request.user.is_superuser:
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '02':   # group leader
                fieldsets = (fieldsets[0], fieldsets[1], fieldsets[5])
                fields = []
                for s in fieldsets:
                    for f in s[1]["fields"]:
                        fields.append(f)
                self.readonly_fields = tuple(fields)
            elif vol_info.level == '03':
                pass

        return fieldsets

    list_display = ["name", "nick_name", "phone_number", "created_at", "status"]
admin.site.register(models.Volunteer, VolunteersAdmin)


class VolunteerGroupAdmin(CustomModelAdmin):
    filter_horizontal = ('volunteers',)
    def queryset(self, request):
        qs = super(CustomModelAdmin, self).queryset(request).filter(status='1')
        if not request.user.is_superuser:
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '01':   # normal volunteer
                qs = None
            elif vol_info.level == '02':   # group leader
                qs = qs.filter(group_leader=vol_info.id)
            elif vol_info.level == '03':  # operator
                qs = qs.filter(school_for_work__in=db_utils.get_operators_schools(vol_info.id))

        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super(VolunteerGroupAdmin, self).get_form(request, obj=None, **kwargs)
        if not request.user.is_superuser:
            vol_info = models.Volunteer.objects.get(user_id=request.user.id)
            if vol_info.level == '02':   # group leader
                region_schools = db_utils.get_group_leader_schools(vol_info)
            elif vol_info.level == '03':  # operator
                region_schools = db_utils.get_operators_schools(vol_info.id)
            form.base_fields["school_for_work"].queryset = region_schools

        return form
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


class OperatorRegionAdmin(CustomModelAdmin):
    list_display = ["operator", "status"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(OperatorRegionAdmin, self).get_form(request, obj=None, **kwargs)
        form.base_fields["operator"].queryset = models.Volunteer.objects.filter(level="03")

        return form

admin.site.register(models.OperatorRegion, OperatorRegionAdmin)