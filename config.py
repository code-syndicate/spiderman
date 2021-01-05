from django.contrib.admin import AdminSite
from users.models import User

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
