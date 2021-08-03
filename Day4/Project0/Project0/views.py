# Created by me - Asif Shaikh
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")