from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('yuna.views',
    url(r'^$', 'home', name='home'),
#    url(r'^signin/$', auth_views.login),
#    url(r'^signout/$', auth_views.logout),

    url(r'^admin/', include(admin.site.urls)),
)
