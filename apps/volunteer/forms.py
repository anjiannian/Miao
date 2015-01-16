# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from models import Volunteer, Activity
from utils import _


class VolunteerForm(ModelForm):
    free_time = forms.CharField(widget=forms.HiddenInput, required=True)

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields["why_in"].help_text = "请至少写3点"

    class Meta:
        model = Volunteer
        exclude = ('user', 'status')


class CreationUserForm(forms.Form):
    email = forms.EmailField(label=_("邮件"), required=True)
    username = forms.RegexField(
        label=_("用户名称"), max_length=30,
        regex=r'^[\w.@+-]+$',
        #help_text=_("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    password1 = forms.CharField(label=_("密码"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("重复密码"),
                                widget=forms.PasswordInput,)
                                #help_text=_("Enter the same password as above, for verification."))

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            "用户名称已存在",
            code='duplicate_username',
        )

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 6:
            raise forms.ValidationError(
                "密码长度必须大于6位",
                code='password_invalid_length',
            )
        return password1


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "两次密码不一致",
                code='password_mismatch',
            )
        return password2


class ActivityForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        # self.fields["why_in"].help_text = "请至少写3点"

    class Meta:
        model = Activity
        # exclude = ('user', 'status')