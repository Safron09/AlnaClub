from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              
    # path('investors/', views.investors, name='investors'),  
    # path('developers/', views.developers, name='developers'),     
    path('how_it_works/', views.how_it_works, name='how_it_works'),      
    path('faq/', views.faq, name='faq'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('our story/', views.our_story, name='our_story'),  
    path('team/', views.team, name='team'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')
]