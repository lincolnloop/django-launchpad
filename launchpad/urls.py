from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Signup.as_view(), name="launchpad_signup"),
    url(r'^success/$', views.Success.as_view(), name="launchpad_success"),
    url(r'^unsubscribe/(?P<key>[\d\w]+)/$', views.Unsubscribe.as_view(),
        name="launchpad_unsubscribe"),
)