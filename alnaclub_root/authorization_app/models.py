from django.contrib.auth.models import AbstractUser
from django.db import models

class InvestorAuthUser(AbstractUser):
    ROLE_CHOICES = [
        ('', 'Select Role'),
        ('Investor', 'Investor'),
        ('Developer', 'Developer'),
        ('Dual', 'Dual'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='', blank=True, null=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    occupation = models.CharField(max_length=255, blank=True, null=True)
    ready_to_invest = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    return_goals = models.TextField(blank=True, null=True)
    projects_done = models.IntegerField(blank=True, null=True)
    ssn = models.CharField(max_length=11, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure non-superusers have a role
        if not self.is_superuser and not self.role:
            raise ValueError("Non-superuser accounts must have a role.")
        super().save(*args, **kwargs)
