from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    PROGRESS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    roi = models.DecimalField(max_digits=5, decimal_places=2, help_text="Return on Investment in %")
    funds_needed = models.DecimalField(max_digits=12, decimal_places=2, help_text="Funds needed in USD")
    estimated_completion_time = models.IntegerField(help_text="Approximate time to completion in days")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    work_progress = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default='To Do')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def approve(self):
        """SuperAdmin approves project"""
        self.status = 'Approved'
        self.save()

    def reject(self):
        """SuperAdmin rejects project"""
        self.status = 'Rejected'
        self.save()

    def __str__(self):
        return f"{self.title} - {self.developer.username}"
