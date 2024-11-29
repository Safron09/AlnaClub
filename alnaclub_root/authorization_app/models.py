
from django.contrib.auth.models import AbstractUser
from django.db import models

class InvestorAuthUser(AbstractUser):
    name = models.CharField(max_length=255, blank=False)  # Required field
    last_name = models.CharField(max_length=255, blank=False)  # Required field
    company_name = models.CharField(max_length=255, blank=True)  # Optional
    email = models.EmailField(unique=True, blank=False)  # Required and used for login
    phone_number = models.CharField(max_length=15, blank=False)  # Required
    address = models.TextField(blank=False)  # Required
    occupation = models.CharField(max_length=255, blank=True)  # Optional
    ready_to_invest = models.DecimalField(max_digits=12, decimal_places=2, blank=False)  # Required
    return_goals = models.TextField(blank=True)  # Optional

    def __str__(self):
        return self.username
