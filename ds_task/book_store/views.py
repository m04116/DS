from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Author, Book
from .forms import AuthorForm, BookForm


class AuthorListView(generic.ListView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm

    def get_success_url(self):
        return reverse('authors')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm

    def get_success_url(self):
        return reverse('authors')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

    # delete without confirmation
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


class BookListView(generic.ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('books')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('books')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

    # delete without confirmation
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
