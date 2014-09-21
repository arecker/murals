from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Portfolio.views.get_home', name='home'),
    url(r'^contact/$', 'Portfolio.views.get_contact', name='contact'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[\w-]+)/$', 'Portfolio.views.get_gallery', name='gallery')
)

urlpatterns += patterns('', url(r'^(?P<slug>[-\w\d]+)', 'Portfolio.views.get_gallery'))
