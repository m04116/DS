from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Book, Request
from .forms import BookForm


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


class RequestsListView(generic.ListView):
    model = Request
    template_name = 'book_store/requests.html'
    queryset = Request.objects.all()[:10]
