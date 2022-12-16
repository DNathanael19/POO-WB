from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, "hello/index.html")
def jayan(request):
	return HttpResponse("Hello, Jayan")
def wilsan(request):
	return HttpResponse("Hello, Wilsan ")
def greet(request, name):
	return render(request, "hello/greet.html",
	 {"name": name.capitalize()})

