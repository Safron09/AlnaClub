from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),                  
    path('how_it_works/', views.how_it_works, name='how_it_works'),      
    path('faq/', views.faq, name='faq')
]