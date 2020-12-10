from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

#Wallet 

class Wallet( models.Model ):
	user = models.OneToOneField( get_user_model() , on_delete = models.SET_NULL, null = True )
	
	wallet_address = models.UUIDField( default  = uuid.uuid4 	, unique = True , primary_key = True )
	
	last_modified = models.DateTimeField( auto_now = True , editable = False )
	
	date_created  = models.DateTimeField( auto_now_add = True  , editable = False)
	
	balance = models.CharField( max_length = 25, default = 0 ,  editable = False )
	
	
	CRYPTOS = (
	('Bitcoin','Bitcoin'),
	('Fortron', 'Fortron'),
	('Ethereum', 'Ethereum'),
	('Litecoin','Litecoin'),
	
				)
				
	currency_type = models.CharField( max_length = 25, default = 'Bitcoin' , choices = CRYPTOS )
	
	
	def add(self, amt ):
		self.balance = self.balance + amt
		self.save()
		
		
	def remove(self, amt ):
		if amt  <= self.balance:
			self.balance = self.balance - amt
			self.save()
			
	@property		
	def sym(self):
		t = self.currency_type
		
		if t == 'Bitcoin':
			return 'B'
		if t == 'Fortron':
			return 'Fx'
		if t == 'Ethereum':
			return 'E'
		if t == 'Litecoin':
			return 'L'
			
		return '€'
		
	def __str__(self):
		return self.user.fname + ' wallet'
