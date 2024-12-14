from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.url')),  # Landing page URLs
    path('auth/', include('authorization_app.urls')),  # Authorization app URLs
]
