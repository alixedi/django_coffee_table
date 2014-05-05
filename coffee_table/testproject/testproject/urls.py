from django.conf.urls import patterns, url
from django.views.generic import ListView

from testapp.models import StarWar


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=StarWar)),
)
