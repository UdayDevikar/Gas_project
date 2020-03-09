from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render

# Create your views here.



def main(request):
	return render (request, 'main.html')



def home(request):
	return render (request, 'home.html')





def about(request):
	return render (request, 'about.html')





def  services(request):
	return render (request, 'services.html')


