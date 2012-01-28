from django.conf.urls.defaults import patterns, include, url
from views import BlogView, PostView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeon.views.home', name='home'),
     url(r'^$', BlogView.as_view(), name='blog'),
     url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='post_view'),
)
