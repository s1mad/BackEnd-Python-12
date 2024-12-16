'''Конечные точки'''


from django.urls import path
from .views import (
    main,
    add_author, get_authors, update_author, delete_author,
    add_book, get_books, update_book, delete_book,
    get_books_by_author, get_sorted_books, get_book_detail, get_books_sql
)


urlpatterns = [
    path('main/', main, name='main'),

    path('authors/add/', add_author, name='add_author'),
    path('authors/', get_authors, name='authors'),
    path('authors/update/<int:author_id>/', update_author, name='update_author'),
    path('authors/delete/<int:author_id>/', delete_author, name='delete_author'),

    path('books/add/', add_book, name='add_book'),
    path('books/', get_books, name='books'),
    path('books/update/<int:book_id>/', update_book, name='update_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),

    path('authors/<int:author_id>/books/', get_books_by_author, name='books_by_author'),
    path('books/sorted/', get_sorted_books, name='sorted_books'),
    path('books/<int:book_id>/', get_book_detail, name='book_detail'),
    path('books/sql/', get_books_sql, name='books_sql'),
]
