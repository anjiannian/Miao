#-*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('apps.volunteer',
    url(r'^$', 'views.index'),
    url(r'^error/$', 'views.error'),

    url(r'^account/register/$', 'views.register_user'),
    url(r'^account/login/$', 'views.login_view'),
    url(r'^account/password_change/$', 'views.password_change_view'),
    url(r'^account/password_change_done/$', 'views.password_change_done'),
    url(r'^account/logout/$', 'views.logout'),

    url(r'^volunteer/apply/(?P<user_id>.*)/$', 'views.volunteer_apply'),
    url(r'^volunteer/history/(?P<user_id>.*)/$', 'views.volunteer_history'),
    url(r'^volunteer/home/(?P<user_id>.*)/$', 'views.user_home'),
    url(r'^volunteer/status/(?P<user_id>.*)/$', 'views.volunteer_status'),

)
urlpatterns += patterns(
    url(r'^static/(?P<path>.*)$', 'django.views.static.server',
        {'document_root': settings.STATIC_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
