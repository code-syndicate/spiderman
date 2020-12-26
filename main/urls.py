from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [

path('<uuid:pk>/dashboard/', views.dashboard_view, name = 'dashboard_view' ),

path( '' , views.home_view, name = 'home_view' ),

path('about-us/' , views.about_view , name = 'about_view' ),


path('contact-us/' , views.contact_view , name = 'contact_view' ),



path('faq/' , views.faq_view , name = 'faq_view' ),


path('thank-you/' , views.thank_view , name = 'thank_view' ),


	]