from django.contrib import admin
from django.urls import path, include
from landing_page.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('', include('landing_page.url')),  # Landing page URLs
    path('auth/', include('authorization_app.urls')),  # Authorization app URLs
]
