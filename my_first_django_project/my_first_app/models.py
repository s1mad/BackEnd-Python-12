'''Модели'''


from django.db import models


class Author(models.Model):
    '''Модель автора'''
    objects = models.Manager()
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return str(self.name)


class Publisher(models.Model):
    '''Модель издателя'''
    objects = models.Manager()
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    '''Модель жанра'''
    objects = models.Manager()
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    '''Модель книги'''
    objects = models.Manager()
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, null=True, blank=True)
    genres = models.ManyToManyField(Genre, null=True, blank=True)

    def __str__(self):
        return str(self.title)
