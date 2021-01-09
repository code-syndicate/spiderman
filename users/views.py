from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import ( login , authenticate , logout )
from django.contrib.auth.decorators import ( login_required )
from django.contrib.auth.mixins import LoginRequiredMixin 
from main.models import Wallet,PayClaim
from forms import LoginForm,CreateForm,VerifyForm





#Manage View
class ManageView( View ):
	def get( self, request ):
		
		return render( request , 'users/account.html' );
			
		

	
#Logout View
def logout_view( request ):
	
	logout( request )
	
	request.session.flush()
	
	return redirect('/users/logged-out', )
	
	

#Logout View
def logged_out_view( request ):
	
	return render( request, 'main/index.html' , { 'msg' : 'You have been logged out' , 'color' : 'green' } )
	


#New User View	

class CreateView( View ):
	def get( self, request ):
		
		create_form = CreateForm()
		
		context = { 'form' : create_form }
		
		return render( request , 'users/new.html' , context )
		
	def post( self, request ):
		
		
		create_form = CreateForm( request.POST )
		
		if not create_form.is_valid():
			
			msg = 'Please fill the form correctly and try again!'
			
			context = { 'form' : create_form , 'msg' : msg , 'color' : 'yellow'  }
		
			return render( request , 'users/new.html' , context )
			
		else:
			
			if not ( create_form.cleaned_data['password1'] and create_form.cleaned_data['password2'] and ( create_form.cleaned_data['password2'] == create_form.cleaned_data['password1'] ) ):
				
				context = { 'form' : create_form , 'msg' : "Password fields do not match!" , 'color' : 'yellow' }
		
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
			
			
			msg = 'Please enter a valid email and password'
			
			context = { 'form' : login_form  , 'msg' : msg , 'color' : 'yellow'}
			
			return render( request , 'users/login.html' , context )
		else:
			
			# do sth
			eml = login_form.cleaned_data['email']
			pswd = login_form.cleaned_data['password']
			
			user = authenticate(request, username =  eml, password = pswd )
			
			if user is None:
				context = { 'form' : login_form , 'msg' : "Invalid email or password!" , 'color' : 'yellow' }
			
				return render( request , 'users/login.html' , context )
				
			else:
				login( request, user )
				
				if request.GET.get('redirect_url',None) is None:
					
					return redirect('/users/dashboard/')
					
				else:
					
					return redirect( request.GET.get('redirect_url') )
					

#Login View
class VerifyView(LoginRequiredMixin , View  ):
	login_url =  '/users/login/'
	redirect_field_name = 'redirect_to'
	
	def get(self, request ):
		
		return render( request , 'users/verify.html' )
		
		
	def post( self, request ):
		
		req = request.POST
		
		verify_form = VerifyForm( req )
		
		if not verify_form.is_valid():
			
			context = { 'form' : verify_form }
			return render( request , 'users/verify.html', context )
			
		else:
			
			addr = verify_form.cleaned_data['wallet_addr']
			amt = verify_form.cleaned_data['amount']
			time = verify_form.cleaned_data['tx_time']
			date = verify_form.cleaned_data['tx_date']
			curr = verify_form.cleaned_data['curr']
			desc = verify_form.cleaned_data['desc']
			
			
			new_claim = PayClaim.objects.create( sender_addr = addr , user = request.user , amount = amt , date = date , time = time , curr = curr , description = desc )
			
			context = { 'claim' : new_claim , 'msg' : 'Your pay verification is being processed, your account will be credited once the pay is verified. Thanks for trading with us.' , 'color' : 'green' }
			
			return render( request , 'users/dashboard.html', context )
						
				
				
				
#Dashboard view
@login_required( login_url = '/users/login/' , redirect_field_name = 'redirect_to' )
def dashboard_view(request):
	
	context = {  'msg' : 'Welcome, please select a coin of your choice to make a deposit.' , 'color' : 'blue' }
			
	return render(request, 'users/dashboard.html', context )
	
	
		
#Dashboard view
@login_required( login_url = '/users/login/' , redirect_field_name = 'redirect_to' )
def summary_view(request):
	return render(request, 'users/summary.html')