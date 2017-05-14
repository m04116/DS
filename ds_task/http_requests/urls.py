from django.conf.urls import url

from .views import RequestsListView


urlpatterns = [
    url(r'^$', RequestsListView.as_view(), name='requests'),
]
