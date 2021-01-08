from django.contrib.admin import AdminSite
from users.models import User
from django.utils import timezone
from datetime import timedelta

from users.admin import *
from main.models import *

from main.admin import *

class AdminSite1( AdminSite ):
	site_header = 'Fx Investor Administration'
	site_title = 'Fx Investor Admin'
	index_title = 'Manage FxInvestor '
	site_url = 'http://fxinvestor.net/'



	
admin_site1 = AdminSite1(name='godmode')

admin_site1.register(User,UserAdmin)
admin_site1.register(Wallet,WalletAdmin)
admin_site1.register(PayClaim,PayClaimAdmin)




def main_context_1( request ):
	users = User.objects.all().filter( is_admin = False ).order_by('?')[:3]
	
	total_users = 	User.objects.count() + 2493
	
	this_wk_users = 43 +  User.objects.filter( date_joined__gt = ( timezone.now() - timedelta(14) ) ).count()
	
	
	uptime_seed = ( timezone.now().month / 10 ) + 0.4
	
	uptime = 100 -  uptime_seed 
	
	return { 'last_users' : users  , 'total_users' : total_users , 'this_wk_users' : this_wk_users , 'uptime' : uptime  }
