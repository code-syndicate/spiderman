from django.contrib import admin
from .models import *





class WalletAdmin(admin.ModelAdmin): 
	fields = ['user' , 'balance' , 'last_modified' ]
	list_display = ('user','balance',)
	list_filter = ['balance','date_created']
	search_fields = ['wallet_address' ]



class PayClaimAdmin(admin.ModelAdmin): 
	fields = []
	list_display = ('user','curr', 'amount','sender_addr','settled','date' , )
	list_filter = ['amount','sender_addr','date','settled','curr']
	search_fields = [ 'amount' ,'sender_addr' ,'curr']
	
	
admin.site.register(Wallet,WalletAdmin)
admin.site.register(PayClaim,PayClaimAdmin)

