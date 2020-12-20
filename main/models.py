from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.


class PayClaim( models.Model ):
	
	user = models.ForeignKey( get_user_model() , related_name = 'withdraw_requests' , on_delete = models.CASCADE )
	
	date = models.DateField()
	
	time = models.TimeField()
	
	amount = models.PositiveIntegerField()
	
	curr = models.CharField(max_length = 25 )
	
	sender_addr = models.CharField( max_length = 64 )
	
	description = models.TextField()
	
	settled = models.BooleanField( default = False )
	
	
	class Meta:
		verbose_name = 'Payment claim'
		verbose_name_plural = 'Payment claims'
	
	

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
