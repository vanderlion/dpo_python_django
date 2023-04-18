from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'main.html')


def translation_example(request, *args, **kwargs):
    return render(request, 'translation_example.html')
