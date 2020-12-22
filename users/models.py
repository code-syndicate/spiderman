import uuid
from django.db import models
from django.contrib.auth.models import ( BaseUserManager , AbstractBaseUser )


# Custom User Manager
class CustomUserManager(BaseUserManager):
	
	def create_user( self, firstname, lastname, email, password ):
		if not firstname:
			raise ValueError("First mame is required!")
		
		if not lastname:
			raise ValueError("Last mame is required!")
		
		if not email:
			raise ValueError("Email Address is required!")
		
		if not password:
			raise ValueError("Password is required!")
			
			
		user = self.model( firstname  = firstname , lastname = lastname , email = self.normalize_email( email) )
		
		user.set_password( password )
		
		user.save( using = self._db )
		
		return user
		
		
	def create_superuser(self, firstname, lastname, email, password ):
		
		user = self.create_user( firstname  = firstname , lastname = lastname , email = email , password = password )
		
		user.is_admin = True
		
		user.save()
		
		return user
		
		


# User Model
class User( AbstractBaseUser ):
	firstname = models.CharField( max_length = 25 , verbose_name = 'firstname'   )
	
	lastname = models.CharField( max_length = 25, verbose_name = 'lastname'   )
	
	email = models.EmailField( max_length = 255, unique = True   )
	
	date_joined = models.DateTimeField( auto_now_add = True  , editable = False )
	
	last_updated = models.DateTimeField( auto_now = True , editable = False  )
	
	id = models.UUIDField( primary_key = True , unique = True , default = uuid.uuid4 , editable = False  )
	
	is_admin = models.BooleanField( default = False )
	
	is_active = models.BooleanField( default = True )
	
	wallet_address = models.CharField( max_length = 72 , unique = True, null = True , editable = False  )
	
	objects = CustomUserManager()
	
	USERNAME_FIELD = 'email'
	
	REQUIRED_FIELDS = ['firstname', 'lastname' ,'password' ]
	
	def __str__(self):
		return self.email
		
	def get_fullname(self):
		return self.firstname + '  ' + self.lastname
		
	@property
	def is_staff(self):
		return self.is_admin
		
	def has_perm(app,label):
		return True
		
	def has_module_perms(app, label):
		return True
		
	