from django.urls import path
from . import views

urlpatterns = [             
    path('investors/', views.investors, name='investors'),  
]