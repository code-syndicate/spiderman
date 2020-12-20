from django import forms
from users.models import User

class CreateForm( forms.ModelForm ):
	
	class Meta:
		model = User
		fields = [ 'firstname' , 'lastname' ,'email' ]
		
	password1 = forms.CharField( required = True , min_length = 8 , max_length = 25 , widget = forms.PasswordInput , label = 'Password' )
	
	password2 = forms.CharField( required = True , min_length = 8 , max_length = 25 , widget = forms.PasswordInput ,label = '	Confirm password' )
	
	
	
class VerifyForm(forms.Form):
	amount = forms.IntegerField( required = True , label = 'Amount ')
	
	desc  = forms.CharField( required = True , max_length = 1024 , min_length = 8, label = 'Description'  )
	
	wallet_addr =  forms.CharField( required = True , max_length = 48 , min_length = 12 , label = 'Address' )
	
	curr = forms.CharField( required = True , max_length = 48 , min_length = 4 , label = 'Currency' )
	
	
	tx_date = forms.DateField( label = 'Transaction date' )
	
	tx_time = forms.TimeField( label = 'Transaction time' )
	
	
	
	
class LoginForm( forms.Form ):
	
	email = forms.EmailField( min_length = 8 , max_length = 255 , required = True )
	
	password = forms.CharField( min_length = 8 , max_length = 25 , required = True , widget = forms.PasswordInput )
	