'''Функции-представления'''


from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from .forms import AuthorForm, BookForm
from .models import Author, Book, Publisher


def main(request):
    '''Страница со всеми вариантами действий'''
    return render(request, 'main.html')


# CRUD для работы с авторами
def add_author(request):
    '''Добавление автора'''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def get_authors(request):
    '''Возвращает всех авторов'''
    authors = Author.objects.all()
    return render(request, 'get_authors.html', {'authors': authors})

def update_author(request, author_id):
    '''Обновляет данные автора'''
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'add_author.html', {'form': form})

def delete_author(request, author_id):
    '''Удаление автора'''
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('authors')


# CRUD для работы с книгами
def add_book(request):
    '''Добавление книги'''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def get_books(request):
    '''Возвращает все книги'''
    books = Book.objects.all()
    return render(request, 'get_books.html', {'books': books})

def update_book(request, book_id):
    '''Обновляет данные книги'''
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})

def delete_book(request, book_id):
    '''Удаление книги'''
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('books')


# Работа с QuerySet API
def get_books_by_author(request, author_id):
    '''Фильтрация книг по автору'''
    books = Book.objects.filter(author_id=author_id)
    return render(request, 'get_books.html', {'books': books})

def get_sorted_books(request):
    '''Сортировка книг по дате'''
    books = Book.objects.values('id', 'title', 'publication_date').order_by('publication_date')
    return render(request, 'get_books.html', {'books': books})

def get_book_detail(request, book_id):
    '''Детали конкретной книги'''
    try:
        book = Book.objects.get(id=book_id)
        total_books = Book.objects.count()
    except ObjectDoesNotExist:
        return render(request, 'main.html')
    return render(request, 'book_detail.html', {'book': book, 'total_books': total_books})

def get_books_sql(request):
    '''Получает все книги, используя sql запрос'''
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM my_first_app_book")
        results = cursor.fetchall()

    # Преобразование списка кортежей result в подхадящий формат
    books = []
    for row in results:
        book = Book(
            id=row[0],
            title=row[1],
            publication_date=row[2],
            author=Author.objects.get(id=row[3]),
        )
        if row[4]:
            book.publisher = Publisher.objects.get(id=row[4])
        books.append(book)

    return render(request, 'get_books.html', {'books': books})
