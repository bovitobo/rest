import platform
import django

from django.shortcuts import render


def main_page(request):
    python_version = platform.python_version()
    django_version = django.get_version()
    context = {'python_version': python_version, 'django_version': django_version}

    return render(request, 'article/index.html', context)
