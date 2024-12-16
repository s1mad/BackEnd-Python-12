'''Формы для работы с моделями'''


from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    '''Форма автора'''
    class Meta:
        '''Данные для формы'''
        model = Author
        fields = ['name', 'birth_date', 'bio']

class BookForm(forms.ModelForm):
    '''Форма книги'''
    class Meta:
        '''Данные для формы'''
        model = Book
        fields = ['title', 'publication_date', 'author', 'publisher', 'genres']
        widgets = {'genres': forms.CheckboxSelectMultiple(),}
