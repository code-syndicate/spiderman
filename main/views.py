from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def dashboard_view(request , pk ):
	
	return HttpResponse(" Dashboard page" )
	

def contact_view(request):
	
	return render(request, 'main/contact_us.html' )

def about_view(request):
	
	return render(request, 'main/about_us.html' )


def thank_view(request):
	
	return render(request, 'main/thank_you.html' )

def faq_view(request):
	
	return render(request, 'main/faq.html' )	

def home_view(request):
	
	return render(request, 'main/index.html' )
