from django.conf.urls import url

from .views import (AuthorListView, AuthorCreateView, AuthorDeleteView, AuthorUpdateView,
    BookListView, BookCreateView, BookDeleteView, BookUpdateView)

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='books'),
    url(r'^book/create/$', BookCreateView.as_view(), name='book_create'),
    url(
        r'^book/(?P<pk>\d+)/update/$',
        BookUpdateView.as_view(),
        name='book_update'),
    url(
        r'^book/(?P<pk>\d+)/delete/$',
        BookDeleteView.as_view(),
        name='book_delete'),

    url(r'^authors/$', AuthorListView.as_view(), name='authors'),
    url(r'^author/create/$', AuthorCreateView.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$',
        AuthorUpdateView.as_view(),
        name='author_update'),
    url(
        r'^author/(?P<pk>\d+)/delete/$',
        AuthorDeleteView.as_view(),
        name='author_delete')
]
