from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def dashboard_view(request , pk ):
	
	return HttpResponse(" Dashboard page" )



def home_view(request):
	
	return render( request , 'main/base.html' )
	