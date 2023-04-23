from django.db import models


class Author(models.Model):
    """ Создаем класс Автор с полям:
    :param name: имя
    :type name: str
    :param family: фамилия
    :type family: str
    :param birth_year: год рождения
    :type birth_year: int
    """
    name = models.CharField(max_length=200, verbose_name='имя автора')
    family = models.CharField(max_length=200, verbose_name='фамилия автора')
    birth_year = models.IntegerField(verbose_name='год рождения')


class Book(models.Model):
    """ Создаем класс Книга с полям: название, автор, isbn, год выпуска, количество страниц"""
    title = models.CharField(max_length=200, verbose_name='название книги')
    author = models.ForeignKey(Author, default=1, on_delete=models.DO_NOTHING, verbose_name='автор книги')
    isbn = models.TextField(blank=False, verbose_name='международный стандартный книжный номер')
    year = models.IntegerField(verbose_name='год выпуска')
    pages = models.IntegerField(verbose_name='количество страниц')
