from django import forms
from users.models import User

class CreateForm( forms.ModelForm ):
	
	class Meta:
		model = User
		fields = [ 'firstname' , 'lastname' ,'email' ]
		
	password1 = forms.CharField( required = True , min_length = 8 , max_length = 25 , widget = forms.PasswordInput , label = 'Password' )
	
	password2 = forms.CharField( required = True , min_length = 8 , max_length = 25 , widget = forms.PasswordInput ,label = '	Confirm password' )
	
	
class LoginForm( forms.Form ):
	
	email = forms.EmailField( min_length = 8 , max_length = 255 , required = True )
	
	password = forms.CharField( min_length = 8 , max_length = 25 , required = True , widget = forms.PasswordInput )
	