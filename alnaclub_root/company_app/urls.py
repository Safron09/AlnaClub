from django.urls import path
from . import views

urlpatterns = [             
    path('our story/', views.our_story, name='our_story'),  
    path('team/', views.team, name='team'),
    path('contact_us/', views.contact_us, name='contact_us'), 
]