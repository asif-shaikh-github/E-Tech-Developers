# Created by me - Asif Shaikh
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World \n This is Asif Shaikh")

def home(request):
    return HttpResponse("This is home page of Bivteo.com")