from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

class UserAdmin(admin.ModelAdmin): 
	fields = ['email' , 'firstname' , 'lastname' ]
	list_display = ('firstname','lastname','email','last_updated')
	list_filter = ['firstname', 'lastname' ,'date_joined']
	search_fields = ['id' ,'email' ,'firstname' ,'wallet_address' ]

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
