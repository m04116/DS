from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date


from .models import Author, Book


class AuthorForm(forms.ModelForm):

	class Meta:
		model = Author
		fields = '__all__'


class BookForm(forms.ModelForm):
	# published_date = forms.DateField(
	# 	widget=forms.SelectDateWidget, initial=date.today)

	class Meta:
		model = Book
		fields = ['title', 'author', 'price', 'isbn', 'published_date',]
		widgets = {'published_date': forms.SelectDateWidget}
