# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from forms import VolunteerForm, CreationUserForm
from models import Volunteer
from settings import LOGIN_URL


def _get_current_username(request):
    if request.user.is_authenticated():
        return request.user
    else:
        return ""


@csrf_protect
def register_user(request):
    if request.method == "GET":
        data = {
            "user_form": CreationUserForm()
        }
        return render_to_response("register.html", data, context_instance=RequestContext(request))
    else:  # POST
        user_form = CreationUserForm(request.POST)
        data = {}
        if user_form.is_valid():
            new_user = User.objects.create_user(
                user_form.cleaned_data["username"],
                user_form.cleaned_data["email"],
                user_form.cleaned_data["password1"]
            )
            new_user.is_superuser = 0
            new_user.is_active = 1
            new_user.is_staff = 0
            new_user.save()
            data["message"] = "保存成功"
            data["username"] = new_user.username

            return HttpResponseRedirect("/home/%s/" % new_user.id)
        else:
            data["user_form"] = user_form

            return render_to_response("register.html", data, context_instance=RequestContext(request))


@csrf_protect
@login_required(login_url=LOGIN_URL)
def user_home(request, user_id):
    data = {
        "username": _get_current_username(request)
    }
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        data["message"] = "用户不存在"
        data["back_url"] = request.META["HTTP_REFERER"]
        return render_to_response("error.html", data,
                                  context_instance=RequestContext(request))
    data["user_info"] = vars(user)
    return render_to_response("user_home.html", data, context_instance=RequestContext(request))


@csrf_protect
@login_required(login_url=LOGIN_URL)
def volunteer_apply(request, user_id):
    # before register volunteer, the user must be the system's user
    template_name = "apply_volunteer.html"
    data = {
        "username": _get_current_username(request)
    }

    if request.method == "GET":
        data["volunteer_form"] = VolunteerForm()
        return render_to_response(template_name, data,
                                  context_instance=RequestContext(request))
    else:  # POST
        volunteer_form = VolunteerForm(request.POST)
        if volunteer_form.is_valid():
            volunteer_model = Volunteer.objects.filter(user_id=user_id)
            if len(volunteer_model) > 0:
                data["message"] = "您的申请已递交, 请勿重复提交。请等待管理员联系。 谢谢您的参与！"
            else:
                exist_user = User.objects.get(id=user_id)
                data["message"] = "您的申请已递交，请等待管理员联系。 谢谢您的参与！"
                volunteer_model = volunteer_form.save(commit=False)
                volunteer_model.free_time = request.POST.get("free_time")
                volunteer_model.user_id = exist_user.id
                volunteer_model.status = 0

                volunteer_model.save()
            data["volunteer_form"] = volunteer_form

        else:
            data["volunteer_form"] = volunteer_form

        return render_to_response(template_name, data, context_instance=RequestContext(request))


def index(request):
    data = {
        "username": _get_current_username(request)
    }
    return render_to_response("index.html", data, context_instance=RequestContext(request))


@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect("/home/%s/" % user.id)
            else:
                data = {
                    "error_msg": "当前用户无法登陆"
                }
                return render_to_response('login.html', data, context_instance=RequestContext(request))
        else:
            data = {
                "error_msg": "用户名称密码错误"
            }
            return render_to_response('login.html', data, context_instance=RequestContext(request))
    else:
        # GET

        return render_to_response('login.html', context_instance=RequestContext(request))


@csrf_protect
@login_required(login_url=LOGIN_URL)
def password_change_view(request):
    from django.contrib.auth.views import password_change

    return password_change(request, template_name="change_password.html",
                           post_change_redirect="/account/password_change_done/")


def password_change_done(request):
    from django.contrib.auth.views import password_change_done

    return password_change_done(request, template_name='change_password_done.html')


def logout(request):
    from django.contrib.auth import logout

    logout(request)

    return HttpResponseRedirect("/")
