from .models import Blog, Author, Entry, EntryDetail
from django import forms


class BlogForm(forms.ModelForm):
    model = Blog
    field = ['name', 'tagline']


class AuthorForm(forms.ModelForm):

    model = Author
    fields = ['name', 'email']

class EntryForm(forms.ModelForm):
    model = Entry
    fields = ['headline', 'body_text', 'n_comments', 'n_pingbacks', 'rating']
