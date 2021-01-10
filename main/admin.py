from django.contrib import admin
from .models import *



class WithdrawalRequestAdmin(admin.ModelAdmin): 
	fields = ['client' , 'amount' , 'mode'  ]
	list_display = ('client' , 'amount' , 'mode' ,'date_filed' ,'settled' )
	list_filter = ['client' , 'mode' , 'settled' ]
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

