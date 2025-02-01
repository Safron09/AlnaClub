from django.urls import path
from .views import (
    developers, add_project, update_project, delete_project,
    superadmin_dashboard, approve_project, reject_project
)

urlpatterns = [             
    path('developers/', developers, name='developers'),  
    path('developers/add/', add_project, name='add_project'),
    path('developers/update/<int:project_id>/', update_project, name='update_project'),
    path('developers/delete/<int:project_id>/', delete_project, name='delete_project'),

    path('superadmin/', superadmin_dashboard, name='superadmin_dashboard'),
    path('superadmin/approve/<int:project_id>/', approve_project, name='approve_project'),
    path('superadmin/reject/<int:project_id>/', reject_project, name='reject_project'),
]
