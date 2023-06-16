from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def conditions(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'conditions.html',d)
def loop(request):
    d={'name':'RAMAKANTH YADAV','age':20,'cls':'python'}
    return render(request,'loop.html',d)