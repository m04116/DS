from datetime import date

from django import forms

from .models import Book


class BookForm(forms.ModelForm):
	published_date = forms.DateField(
		widget=forms.SelectDateWidget, initial=date.today)

	class Meta:
		model = Book
		fields = ['title', 'author', 'price', 'isbn', 'published_date',]
