from django.urls import path
from .import views

urlpatterns = [

path('<uuid:pk>/dashboard/', views.dashboard_view, name = 'dashboard_view' ),

path( '' , views.home_view, name = 'home_view' ),



	]