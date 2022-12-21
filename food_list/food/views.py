from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return HttpResponse('Hello World')


def item(request):
	return HttpResponse("This is an item view")
