
from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    context = {
        'test1' : "test 1 successful"
    }
    return render(request, 'home.html', context)