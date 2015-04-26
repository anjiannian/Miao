#-*- coding: UTF-8 -*-
import os
from django import template
register = template.Library()

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

SUBMIT_LINE_HTML = os.path.normpath(
    os.path.join(CURRENT_PATH, '../../../templates/admin/custom_submit_line.html')
)
@register.inclusion_tag(SUBMIT_LINE_HTML, takes_context=True)
def custom_submit_line(context):
    curr_user = context["user"]
    opts = context['opts']
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    # if user has view only permission than show none buttons
    view_only_perm = curr_user.has_perm("%s.%s" % (str(opts).split(".")[0], "view_only_" + str(opts).split(".")[1]))
    ctx = {
        'opts': opts,
        'show_delete_link': (not is_popup and context['has_delete_permission']
                              and change and context.get('show_delete', True)),
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': context['has_add_permission'] and
                            not is_popup and (not save_as or context['add']),
        'show_save_and_continue': not is_popup and context['has_change_permission'],
        'is_popup': is_popup,
        'show_save': True,
        'preserved_filters': context.get('preserved_filters'),
        'view_only_perm': (view_only_perm and not curr_user.is_superuser)
    }

    if context.get('original') is not None:
        ctx['original'] = context['original']
    return ctx



ACTIVITY_SUBMIT_LINE_HTML = os.path.normpath(
    os.path.join(CURRENT_PATH, '../../../templates/admin/activity_submit_line_publish.html')
)
@register.inclusion_tag(ACTIVITY_SUBMIT_LINE_HTML, takes_context=True)
def activity_submit_line_publish(context):
    curr_user = context["user"]
    opts = context['opts']
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    # if user has view only permission than show none buttons
    view_only_perm = curr_user.has_perm("%s.%s" % (str(opts).split(".")[0], "view_only_" + str(opts).split(".")[1]))
    ctx = {
        'opts': opts,
        'show_delete_link': (not is_popup and context['has_delete_permission']
                              and change and context.get('show_delete', True)),
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': context['has_add_permission'] and
                            not is_popup and (not save_as or context['add']),
        'show_save_and_continue': not is_popup and context['has_change_permission'],
        'is_popup': is_popup,
        'show_save': True,
        #for activity confirmed
        'show_confirm': True,
        'preserved_filters': context.get('preserved_filters'),
        'view_only_perm': (view_only_perm and not curr_user.is_superuser)
    }

    if context.get('original') is not None:
        ctx['original'] = context['original']
    return ctx


ACTIVITY_SUBMIT_LINE_HTML = os.path.normpath(
    os.path.join(CURRENT_PATH, '../../../templates/admin/activity_submit_line_confirm.html')
)
@register.inclusion_tag(ACTIVITY_SUBMIT_LINE_HTML, takes_context=True)
def activity_submit_line_confirm(context):
    curr_user = context["user"]
    opts = context['opts']
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    # if user has view only permission than show none buttons
    view_only_perm = curr_user.has_perm("%s.%s" % (str(opts).split(".")[0], "view_only_" + str(opts).split(".")[1]))
    ctx = {
        'opts': opts,
        'show_delete_link': (not is_popup and context['has_delete_permission']
                              and change and context.get('show_delete', True)),
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': context['has_add_permission'] and
                            not is_popup and (not save_as or context['add']),
        'show_save_and_continue': not is_popup and context['has_change_permission'],
        'is_popup': is_popup,
        'show_save': True,
        #for activity confirmed
        'show_confirm': True,
        'preserved_filters': context.get('preserved_filters'),
        'view_only_perm': (view_only_perm and not curr_user.is_superuser)
    }

    if context.get('original') is not None:
        ctx['original'] = context['original']
    return ctx