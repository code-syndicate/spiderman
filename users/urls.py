from django.urls import path
from .import views


app_name = 'users'


urlpatterns = [

path('logout/', views.logout_view , name = 'logout_view' ) ,

path( 'new/', views.CreateView.as_view() , name = 'create_view' ),

path( 'dashboard/', views.dashboard_view , name = 'dashboard_view' ),

path( 'summary/', views.summary_view , name = 'summary_view' ),

path( 'login/', views.LoginView.as_view() , name = 'login_view' ),




	]