#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
Django settings for Miao project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + "/Miao/"

import siteuser

APPEND_SLASH = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2gzsj2#z5q8s+s3!tsl*pll-kazek(rvf$9^i!_29t48_mky1*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.volunteer',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'siteuser.middleware.User',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'miao',
        'USER': 'miao_mysql',
        'PASSWORD': "123456",
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh_cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = BASE_DIR + '/static/'   #  use python manage.py collectstatic . to collect all static files
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/media/'


TEMPLATE_DIRS = (
    siteuser.SITEUSER_TEMPLATE,
    BASE_DIR + "templates/volunteer/",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    'siteuser.context_processors.social_sites',

)

AVATAR_DIR = STATIC_ROOT + 'img/avatar/'   # 头像上传目录
SITEUSER_EMAIL = {
    'smtp_host': 'smtp.gmail.com',
    'smtp_port': 25,
    'username': 'xxx',
    'password': 'xxx',
    'from': 'xxx@gmail.com',
    'display_from': '',
}

class SITEUSER_ACCOUNT_MIXIN(object):
    login_template = 'login.html'           # 你项目的登录页面模板
    register_template = 'register.html'     # 你项目的注册页面模板
    reset_passwd_template = 'reset_password.html'   # 忘记密码的重置密码模板
    change_passwd_template = 'change_password.html' # 登录用户修改密码的模板
    reset_passwd_email_title = u'重置密码'    # 重置密码发送电子邮件的标题
    reset_passwd_link_expired_in = 24        # 重置密码链接多少小时后失效
    notify_template = "notify.html"

    def get_login_context(self, request):
        return {}

    def get_register_context(self, request):
        return {}



from django.db import models
class SITEUSER_EXTEND_MODEL(models.Model):
    # some fields...
    test_field = models.CharField(u"测试自动", max_length=12, null=True, blank=True)
    class Meta:
        abstract = True