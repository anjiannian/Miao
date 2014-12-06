from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('apps.volunteer',
    url(r'^$', 'views.index'),
    url(r'^register/$', 'views.register'),
)
urlpatterns += patterns(
    url(r'^static/(?P<path>.*)$', 'django.views.static.server',
        {'document_root': settings.STATIC_ROOT}),
    (r'', include('siteuser.urls')),
    (r'^admin/', include(admin.site.urls)),
)
