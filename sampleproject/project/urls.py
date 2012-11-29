from django.conf.urls import patterns, include, url

# uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^shot/', include('webthumbnailer.urls')),

    # examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
