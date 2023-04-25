from django.urls import path
from app_news.views import get_news_in_custom_format

urlpatterns = [
    path('', get_news_in_custom_format, name='news_list')
]
