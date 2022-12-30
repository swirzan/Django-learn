from django.shortcuts import render
from django.http import HttpResponse

def january(request):
    return HttpResponse('Hello World')

def february(request):
    return HttpResponse('Challenge Completed')
