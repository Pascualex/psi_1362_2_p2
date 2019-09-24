from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    message = "Rango says here is the about page."
    index_page = "Return to the <a href='/rango/'>index page</a>."
    return HttpResponse(message + " " + index_page)
