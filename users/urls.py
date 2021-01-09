from django.urls import path
from .import views


app_name = 'users'


urlpatterns = [

path('logout/', views.logout_view , name = 'logout_view' ) ,

path('logged-out/', views.logged_out_view , name = 'logged_out_view' ) ,

path( 'new/', views.CreateView.as_view() , name = 'create_view' ),

path( 'dashboard/', views.dashboard_view , name = 'dashboard_view' ),

path( 'summary/', views.summary_view , name = 'summary_view' ),

path( 'login/', views.LoginView.as_view() , name = 'login_view' ),

path( 'verify-pay/', views.VerifyView.as_view() , name = 'verify_view' ),


path( 'manage/', views.ManageView.as_view() , name = 'manage_view' ),


path( 'withdraw/', views.ManageView.as_view() , name = 'withdraw_view' ),





	]