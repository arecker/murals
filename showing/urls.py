from django.conf.urls import url

import views


urlpatterns = [url(r'^$',
                   views.Index.as_view(),
                   name='index'),
               url(r'^(?P<slug>[^/]+)/$',
                   views.GalleryDetail.as_view(),
                   name='gallery-detail')]
