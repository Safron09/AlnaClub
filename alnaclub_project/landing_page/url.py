from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              
    path('investors/', views.investors, name='investors'),  
    path('developers/', views.developers, name='developers'),     
    path('how_it_works/', views.how_it_works, name='how_it_works'),      
    path('faq/', views.faq, name='faq'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')     
]