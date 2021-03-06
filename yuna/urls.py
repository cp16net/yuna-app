from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('yuna.views',
    url(r'^favicon\.ico$', RedirectView.as_view(url="/static/favicon.ico")),
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'index'),
    url(r'^logout/$', 'logout'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^signin/$', auth_views.login),
    # url(r'^signout/$', auth_views.logout),
    # url(r'^accounts/profile', 'login_redirect'),
    # url(r'^accounts/', include('social_auth.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('yuna.people.urls', namespace='people')),
)
