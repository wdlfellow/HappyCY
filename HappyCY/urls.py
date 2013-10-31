from django.conf.urls import patterns, include, url
from cy import views
from HappyCY import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #added for project happycy
    url(r'^$', views.index),
    url(r'^index/', views.index),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),
    url(r'^reg/$', views.register),
    url(r'^knowledgepoint/(\d+)/$', views.kptest),
)
