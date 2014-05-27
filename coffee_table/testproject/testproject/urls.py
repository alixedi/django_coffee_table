from django.conf.urls import patterns, url
from django.views.generic import ListView

from testapp.models import StarWar


urlpatterns = patterns('',

    url(r'^basic/$',
        ListView.as_view(model=StarWar, template_name="testapp/basic.html"),
        name='basic'),

    url(r'^paging/$',
        ListView.as_view(model=StarWar, template_name="testapp/paging.html"),
        name='paging'),

    url(r'^help/$',
        ListView.as_view(model=StarWar, template_name="testapp/help.html"),
        name='help'),

    url(r'^check/$',
        ListView.as_view(model=StarWar, template_name="testapp/check.html"),
        name='check'),

    url(r'^css/$',
        ListView.as_view(model=StarWar, template_name="testapp/css.html"),
        name='css'),

    url(r'^pkcol/$',
        ListView.as_view(model=StarWar, template_name="testapp/pkcol.html"),
        name='pkcol'),

    url(r'^full/$',
        ListView.as_view(model=StarWar, template_name="testapp/full.html"),
        name='full'),
)
