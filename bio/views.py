from django.shortcuts import render
from django.http import HttpRequest

def register(request):
    return render(request, 'register.html')

def python(request):
    context = {
        'creator' : ' Guido van Rossum',
        'name' : 'Pyhton',
        'year' : 1991
    }
    return render(request, 'python.html',context )
def c(request):
    context = {
        'creator' : 'Dennis Ritchie',
        'name' : 'C',
        'year' : 1972
    }
    return render(request, 'c.html',context)
def cpp(request):
    context = {
        'creator' : 'Bjarne Stroustrup',
        'name' : 'C++',
        'year' : 1985
    }
    return render(request, 'c++.html',context)
def java(request):
    context = {
        'creator' : 'James Gosling',
        'name' : 'Java',
        'year' : 1995
    }
    return render(request, 'java.html', context)
def end(request):
    return render(request, 'end.html' )