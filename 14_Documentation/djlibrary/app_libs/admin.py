from django.contrib import admin
from app_libs.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'family']

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Book, BookAdmin)
