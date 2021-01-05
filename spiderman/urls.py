
from django.contrib import admin
from django.urls import path, include
from config import admin_site1

urlpatterns = [
    #path('admin/', admin.site.urls),

	
    path('godmode/', admin_site1.urls),

	path( 'users/' , include('users.urls') ),
	
	path( '' , include( 'main.urls' ) ) ,
]
