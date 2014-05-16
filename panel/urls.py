# Copyright (c) 2014 Andros Romo

try:
    from django.conf.urls import url, patterns
except:
    from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('panel.views',
    url(r'^$', 'dashboard', name='dashboard'),
)
