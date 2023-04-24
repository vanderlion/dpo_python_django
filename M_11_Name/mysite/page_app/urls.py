from django.urls import path

from page_app.views import translation_example

urlpatterns = [
    path('example/', translation_example, name='example')
]
