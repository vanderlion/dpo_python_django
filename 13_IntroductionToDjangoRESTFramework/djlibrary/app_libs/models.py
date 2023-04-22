from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя автора')
    family = models.CharField(max_length=200, verbose_name='фамилия автора')
    birth_year = models.IntegerField(verbose_name='год рождения')


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='название книги')
    isbn = models.IntegerField(verbose_name='международный стандартный книжный номер')
    year = models.IntegerField(verbose_name='год выпуска')
    pages = models.IntegerField(verbose_name='количество страниц')
