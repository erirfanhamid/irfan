#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome Irfan Hamid at Django Polls App")
