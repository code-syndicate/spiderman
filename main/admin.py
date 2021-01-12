from django.contrib import admin
from .models import *

class AuthPinAdmin( admin.ModelAdmin ):
	fields = ['is_invalid' ,'for_user' ]
	list_display = ['pin' , 'withdraw_request' ,'for_user' ,'generated_on' , 'used' , 'is_invalid' ]
	list_filter = ['is_invalid' ,'used' ,'for_user','generated_on']
	search_fields = ['pin', ]
	

class WithdrawalRequestAdmin(admin.ModelAdmin): 
	fields = ['settled','desc']
	list_display = ('client' , 'amount' , 'mode' ,'wallet_addr' , 'wallet_type' , 'bank_name' , 'bank_acct_no' , 'bank_swift' , 'date_filed' ,'settled' )
	list_filter = ['client' , 'wallet_type' ,'mode' , 'settled' ]
	search_fields = ['amount', ]


class WalletAdmin(admin.ModelAdmin): 
	fields = ['user' , 'balance' , 'bonus' ]
	list_display = ('user','balance', 'bonus', 'last_modified')
	list_filter = ['balance','date_created']
	search_fields = ['wallet_address' ]



class PayClaimAdmin(admin.ModelAdmin): 
	fields = []
	list_display = ('user','curr', 'amount','sender_addr','settled','date' , )
	list_filter = ['amount','sender_addr','date','settled','curr']
	search_fields = [ 'amount' ,'sender_addr' ,'curr']
	

admin.site.register(Wallet,WalletAdmin)
admin.site.register(PayClaim,PayClaimAdmin)

