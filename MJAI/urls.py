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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
