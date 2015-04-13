# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from forms import ActivityForm
from models import ActivityPublish, VOLUNTEER_STATUS, Volunteer
from settings import LOGIN_URL
import utils

VOLUNTEER_STATUS_DICT = utils.model_choice_2_dict(VOLUNTEER_STATUS)


#=====================================================================
@csrf_protect
@login_required(login_url=LOGIN_URL)
def list_activity(request):
    data = {}
    template_name = "activity_list.html"
    activities = ActivityPublish.objects.all()
    act_form = ActivityForm()

    if not request.user.is_anonymous():
        volunteer_info = Volunteer.objects.filter(user_id=request.user.id)
        if volunteer_info :
            data["volunteer_status"] = volunteer_info[0].status
    data["activities"] = activities
    data["act_form"] =  act_form

    return render_to_response(template_name, data, context_instance=RequestContext(request))


@csrf_protect
@login_required(login_url=LOGIN_URL)
def application(request, choice, user_id):
    template_name = "activity_list.html"

    return render_to_response(template_name, {}, context_instance=RequestContext(request))
