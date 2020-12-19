﻿import uuid
from django.db import models
from django.contrib.auth.models import ( BaseUserManager , AbstractBaseUser )


# Custom User Manager
class CustomUserManager(BaseUserManager):
	
	def create_user( self, firstname, lastname, email, password ):
		if not fname:
			raise ValueError("First mame is required!")
		
		if not lname:
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
		
		user = self.create_user( firstname  = firstname , lastname = lastname , email = 7 , password = password )
		
		user.is_admin = True
		
		user.save()
		
		return user
		
		


# User Model
class User( AbstractBaseUser ):
	firstname = models.CharField( max_length = 253 , verbose_name = 'firstname' )
	
	lastname = models.CharField( max_length = 254 , verbose_name = 'lastname' )
	
	email = models.EmailField( max_length = 255, unique = True )
	
	date_joined = models.DateTimeField( auto_now_add = True )
	
	last_updated = models.DateTimeField( auto_now = True )
	
	id = models.UUIDField( primary_key = True , unique = True , default = uuid.uuid4 )
	
	is_admin = models.BooleanField( default = False )
	
	is_active = models.BooleanField( default = True )
	
	wallet_address = models.CharField( max_length = 256, unique = True, null = True )
	
	objects = CustomUserManager()
	
	USERNAME_FIELD = 'email'
	
	REQUIRED_FIELDS = ['firstname', 'lastname' ,'password' ]
	
	def __str__(self):
		return self.email
		
	def get_fullname(self):
		return self.firstname + '  ' + self.lastname
		
	@property
	def is_superuser(self):
		return self.is_admin
		
	def has_perms(app, label):
		return True
		
	