from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import ( login , authenticate , logout )
from django.contrib.auth.decorators import ( login_required )
from main.models import Wallet
from forms import LoginForm,CreateForm


#Logout View
def logout_view( request ):
	
	logout( request )
	
	request.session.flush()
	
	return redirect('/')


#New User View	

class CreateView( View ):
	def get( self, request ):
		
		create_form = CreateForm()
		
		context = { 'form' : create_form }
		
		return render( request , 'users/new.html' , context )
		
	def post( self, request ):
		
		
		create_form = CreateForm( request.POST )
		
		if not create_form.is_valid():
			
			context = { 'form' : create_form }
		
			return render( request , 'users/new.html' , context )
			
		else:
			
			if not ( create_form.cleaned_data['password1'] and create_form.cleaned_data['password2'] and ( create_form.cleaned_data['password2'] == create_form.cleaned_data['password1'] ) ):
				
				context = { 'form' : create_form , 'msg' : "Password fields do not match!" }
		
				return render( request , 'users/new.html' , context )
			
			pre_saved_user = create_form.save( commit = False )
			
			pre_saved_user.set_password( create_form.cleaned_data['password2'] )
			
			pre_saved_user.save()
			
			new_wallet = Wallet.objects.create( user = pre_saved_user )
			
			new_wallet.save()
			
			pre_saved_user.wallet_address = new_wallet.wallet_address
			
			pre_saved_user.save()
			
			request.session.flush()
		
			return  redirect('/users/login/')

	

#Login View
class LoginView( View ):
	def get( self, request ):
		
		if request.user.is_authenticated:
			return redirect(reverse('users:dashboard_view'))
			
		login_form = LoginForm()
		
		context = { 'form' : login_form }
		
		return  render( request , 'users/login.html' , context )
		
		
	def post( self, request ):
		
		
		login_form = LoginForm( request.POST )
		
		if not login_form.is_valid():
			
			context = { 'form' : login_form }
			
			return render( request , 'users/login.html' , context )
		else:
			
			# do sth
			eml = login_form.cleaned_data['email']
			pswd = login_form.cleaned_data['password']
			
			user = authenticate(request, username =  eml, password = pswd )
			
			if user is None:
				context = { 'form' : login_form , 'msg' : "Sorry, the details you provided are incorrect!"  }
			
				return render( request , 'users/login.html' , context )
				
			else:
				login( request, user )
				
				if request.GET.get('redirect_url',None) is None:
					
					return redirect('/users/dashboard/')
					
				else:
					
					return redirect( request.GET.get('redirect_url') )
					

#Login View
class VerifyView( View ):
	def get( self, request ):
		
		
		return  render( request , 'users/verify.html' )
		
		
	def post( self, request ):
		
		
			return render( request , 'users/verify.html' )
						
				
				
				
#Dashboard view
@login_required( login_url = '/users/login/' , redirect_field_name = 'redirect_to' )
def dashboard_view(request):
	return render(request, 'users/dashboard.html')
	
	
		
#Dashboard view
@login_required( login_url = '/users/login/' , redirect_field_name = 'redirect_to' )
def summary_view(request):
	return render(request, 'users/summary.html')