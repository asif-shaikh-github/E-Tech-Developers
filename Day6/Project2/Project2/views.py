from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Home Page</h1> <br> Links to other pages<br> <a href="about">About</a><br><a href="login">Login</a>''')

def about(request):
    return HttpResponse('''<h1>About Page</h1> <br> Links to other pages <br><a href="/">Home</a><br><a href="login">Login</a>''')

def login(request):
    return HttpResponse('''<h1>Login Page</h1> <br>Links to other pages <br><a href="/">Home</a> <br> <a href="about">About</a>''')
