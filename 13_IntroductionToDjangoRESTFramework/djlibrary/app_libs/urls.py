from django.urls import path
from app_libs.views import AuthorList, BookList

urlpatterns=[
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('books/', BookList.as_view(), name='books_list'),
]
