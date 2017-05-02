from django.conf.urls import url

from .views import (
	BookListView, BookCreateView, BookDeleteView, BookUpdateView, RequestsListView
)

urlpatterns = [
	url(r'^books/$', BookListView.as_view(), name='books'),
	url(r'^book/create/$', BookCreateView.as_view(), name='book_create'),
	url(
		r'^book/(?P<pk>\d+)/update/$',
		BookUpdateView.as_view(),
		name='book_update'),
	url(
		r'^book/(?P<pk>\d+)/delete/$',
		BookDeleteView.as_view(),
		name='book_delete'),
	url(r'^requests/$', RequestsListView.as_view(), name='requests'),
]
