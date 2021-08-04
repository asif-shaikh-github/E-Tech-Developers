from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Bivteo.com</h1> <h3>Below are some links to pages you can visit</h3> <a href="https://www.facebook.com/">Visit to Facebook</a> <br><a href="https://www.quora.com">Visit to Quora </a>''')