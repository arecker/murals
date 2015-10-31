from django.conf.urls import url

import views


urlpatterns = [url(r'^$',
                   views.message,
                   name='contact'),

               url(r'^thanks/$',
                   views.Thanks.as_view(),
                   name='contact-thanks')]
