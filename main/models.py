from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.

class AuthPin(models.Model):
	pin  = models.CharField( unique = True , default = uuid.uuid4 , max_length = 72 ,editable = False , primary_key = True ,verbose_name = 'PIN' )
	
	for_user = models.ForeignKey( get_user_model() , related_name = 'pins' , on_delete = models.CASCADE ,verbose_name = 'Ordering Client' )
	
	withdraw_request = models.OneToOneField( 'WithdrawalRequest' , related_name = 'reqs' , on_delete = models.CASCADE , editable = False , null = True  ,verbose_name = 'Matching Withdrawal Request ' )
	
	generated_on = models.DateTimeField( auto_now_add = True  ,verbose_name = 'Generation Date')
	
	used = models.BooleanField( default = False , editable = False  ,verbose_name = 'PIN used')
	
	is_invalid =  models.BooleanField( default = False  ,verbose_name = 'Invalidated By Admin'  )
	
	
	class Meta:
		verbose_name = 'Authentication PIN'
		verbose_name_plural = 'Authentication PINs'
	
	
	
	def __str__(self):
		return self.for_user.email + '  pin[ ' + str(self.pin) + ' ]'

class WithdrawalRequest( models.Model ):
	
	client = models.ForeignKey( get_user_model() , related_name = 'withdrawal_requests' , on_delete = models.CASCADE )
	
	pin = models.CharField( max_length = 48 ,  blank = False )
	
	amount = models.PositiveIntegerField( blank = False )
	
	mode = models.CharField( max_length = 25 , choices = ( ('bank','bank'),('wallet','wallet') )  ,verbose_name = 'Payment Mode' )
	
	wallet_type = models.CharField( max_length = 25 , choices = ( ('bitcoin','bitcoin'),('eth','eth') )   , blank = True , verbose_name = 'Wallet Type' )
	
	wallet_addr = models.CharField( max_length = 72 ,  blank = True , verbose_name = 'Wallet Address' )
	
	bank_name = models.CharField( max_length = 128 ,  blank = True , verbose_name = 'Bank Name' )
	
	bank_acct_no = models.CharField( max_length = 25 ,  blank = True , verbose_name = 'Bank Account Number' )
	
	bank_swift = models.CharField( max_length = 16 ,  blank = True , verbose_name = 'Bank SWIFT' )
	
	date_filed = models.DateTimeField(auto_now_add = True )
	
	settled = models.BooleanField( default  = False , verbose_name = 'Paid' )
	
	desc = models.TextField( verbose_name = 'Description ', blank = True )
	
	class Meta:
		verbose_name = 'Withdrawal Request'
		verbose_name_plural = 'Withdrawal Requests'
	
	
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
		verbose_name = 'Payment Claim'
		verbose_name_plural = 'Payment Claims'
		
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
