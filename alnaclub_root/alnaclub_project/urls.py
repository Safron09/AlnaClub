from django.contrib import admin
from django.urls import path, include
from homepage_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('', include('homepage_app.url')),  # Landing page URLs
    path('auth/', include('authorization_app.urls')),  # Authorization app URLs
    path('investors/', include('investors_app.urls')),
    path('developers/', include('developers_app.urls')),
]
