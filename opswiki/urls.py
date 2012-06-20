from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opswiki.views.home', name='home'),
    # url(r'^opswiki/', include('opswiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
urlpatterns = patterns('',
(r'^opswiki/(?P<page_name>[^/]+)/$',      'opswiki.wiki.views.view_page'),
(r'^10.3.0.249:8000/opswiki/(?P<page_name>[^/]+)/media/$',      'opswiki.media.view_page'),    
)
