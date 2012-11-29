from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^v1/$', 'webthumbnailer.views.get_thumbnail', name='get-thumbnail'),
)
