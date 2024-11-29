from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('landing_page.url')), # Connect the landing_page app
    path('', include('authorization_app.urls')),
]
