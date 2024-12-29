from django.urls import path
from . import views

urlpatterns = [
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')
]
