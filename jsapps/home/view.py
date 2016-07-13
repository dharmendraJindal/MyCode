from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from django.shortcuts import render


def home(request):
    context = {
        'test1' : "test 1 successful"
    }
    return render(request, 'home.html', context)