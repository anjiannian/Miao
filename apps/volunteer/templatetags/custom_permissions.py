#-*- coding: UTF-8 -*-
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def has_view_only_perm(context):
    curr_user = context["user"]
    if curr_user.is_superuser or not context.get('app_label', None):
        return False
    view_only_perm = False
    app_label = context["app_label"]
    has_module_perm = curr_user.has_perm(app_label)
    if has_module_perm:
        model_name = context["app_list"][1]["name"]
        # if user has view only permission than show none buttons
        view_only_perm = curr_user.has_perm("%s.%s" % (app_label, "view_only_" + model_name))
    return has_module_perm and view_only_perm
