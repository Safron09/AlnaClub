from django.contrib import admin
from .models import InvestorAuthUser

@admin.register(InvestorAuthUser)
class InvestorAuthUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'name', 'last_name', 'phone_number']
    list_filter = ['role']  # Add filter for roles
    search_fields = ['username', 'email', 'name', 'last_name']  # Enable search by fields
