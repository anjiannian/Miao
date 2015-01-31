#-*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('apps.volunteer.views',
    url(r'^$', 'index'),
    url(r'^error/$', 'error'),

    url(r'^account/register/$', 'register_user'),
    url(r'^account/login/$', 'login_view'),
    url(r'^account/password_change/$', 'password_change_view'),
    url(r'^account/password_change_done/$', 'password_change_done'),
    url(r'^account/logout/$', 'logout'),

)


urlpatterns += patterns('apps.volunteer.volunteer',
    url(r'^volunteer/apply/(?P<user_id>.*)/$', 'volunteer_apply'),
    url(r'^volunteer/history/(?P<user_id>.*)/$', 'volunteer_history'),
    url(r'^volunteer/home/(?P<user_id>.*)/$', 'user_home'),
    url(r'^volunteer/status/(?P<user_id>.*)/$', 'volunteer_status'),
    url(r'^volunteer/ask_for_leave/(?P<user_id>.*)/$', 'ask_for_leave'),
    url(r'^volunteer/homework/(?P<user_id>.*)/$', 'volunteer_homework'),
)

from django.conf.urls.static import static
urlpatterns += patterns('apps.volunteer.activity',
    url(r'^activity/list/$', 'list_activity'),
    url(r'^activity/apply/(?P<choice>.*)/(?P<user_id>.*)/$', 'application'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    url(r'^static/(?P<path>.*)$', 'django.views.static.server',
        {'document_root': settings.STATIC_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
