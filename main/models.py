from django.db import models
from django.contrib.auth import get_user_model
import uuid

# Create your models here.


class WithdrawalRequest( models.Model ):
	
	client = models.ForeignKey( get_user_model() , related_name = 'withdrawal_requests' , on_delete = models.CASCADE )
	
	pin = models.CharField( max_length = 48 ,  blank = False )
	
	amount = models.PositiveIntegerField( blank = False )
	
	mode = models.CharField( max_length = 25 , choices = ( ('bank','bank'),('wallet','wallet') )  )
	
	wallet_type = models.CharField( max_length = 25 , choices = ( ('bitcoin','bitcoin'),('eth','eth') )   , blank = True )
	
	wallet_addr = models.CharField( max_length = 72 ,  blank = True )
	
	bank_name = models.CharField( max_length = 128 ,  blank = True )
	
	bank_acct_no = models.CharField( max_length = 25 ,  blank = True )
	
	bank_swift = models.CharField( max_length = 16 ,  blank = True )
	
	date_filed = models.DateTimeField(auto_now_add = True )
	
	settled = models.BooleanField( default  = False )
	
	desc = models.TextField()
	
	
	def __str__(self):
		return "Withdrawal Request " + str(self.id) + ' [ ' + str(self.client.email) + ' ]'
	
	


class PayClaim( models.Model ):
	
	user = models.ForeignKey( get_user_model() , related_name = 'withdraw_requests' , on_delete = models.CASCADE )
	
	date = models.DateField()
	
	time = models.TimeField()
	
	amount = models.PositiveIntegerField()
	
	curr = models.CharField(max_length = 25 , verbose_name = 'Currency' )
	
	sender_addr = models.CharField( max_length = 64, verbose_name = 'Sending Wallet Address' )
	
	description = models.TextField()
	
	settled = models.BooleanField( default = False )
	
	
	class Meta:
		verbose_name = 'Payment claim'
		verbose_name_plural = 'Payment claims'
		
	def __str__(self):
		return 'Pay Claim  ' + str(self.id) + ' [ ' + str(self.user.email) +  ' ] '
	
	

#Wallet 

class Wallet( models.Model ):
	user = models.OneToOneField( get_user_model() , on_delete = models.SET_NULL, null = True )
	
	wallet_address = models.UUIDField( default  = uuid.uuid4 	, unique = True , primary_key = True , editable = False  )
	
	last_modified = models.DateTimeField( auto_now = True  )
	
	date_created  = models.DateTimeField( auto_now_add = True  , editable = False)
	
	balance = models.PositiveIntegerField( default = 0  )
	
	
	bonus = models.PositiveIntegerField( default = 0  )
	
	notes = models.TextField()
	
	
	
	def add(self, amt ):
		self.balance = self.balance + amt
		self.save()
		
		
	def remove(self, amt ):
		if amt  <= self.balance:
			self.balance = self.balance - amt
			self.save()
	
		
	def __str__(self):
		return self.user.firstname + ' wallet [ ' + str(self.user.email) + ' ]'
