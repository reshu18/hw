

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show(request):
    return HttpResponse('Hello world this is the first django program')