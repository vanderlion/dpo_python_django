from django.shortcuts import render


def translation_example(request, *args, **kwargs):
    return render(request, 'translation_example.html')
