from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InvestorAuthUser

class InvestorAuthUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Investor', 'Investor'),
        ('Developer', 'Developer'),
        ('Dual', 'Dual'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="User Role") 
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(required=False)  # Optional
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    occupation = forms.CharField(required=False)  # Optional
    ready_to_invest = forms.DecimalField(required=True, max_digits=12, decimal_places=2)
    return_goals = forms.CharField(widget=forms.Textarea, required=False)  # Optional
    projects_done = forms.IntegerField(required=False)
    ssn = forms.CharField(required=True)

    class Meta:
        model = InvestorAuthUser
        fields = [
            'username', 'name', 'last_name', 'company_name', 'email',
            'phone_number', 'address', 'password1', 'password2', 'role',
            'occupation', 'ready_to_invest', 'return_goals', 'projects_done', 'ssn',
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')

        if role == 'Investor':
            if not cleaned_data.get('ready_to_invest') or not cleaned_data.get('return_goals'):
                raise forms.ValidationError("Investor-specific fields are required.")
        elif role == 'Developer':
            if not cleaned_data.get('projects_done'):
                raise forms.ValidationError("Developer-specific fields are required.")
        elif role == 'Dual':
            if not cleaned_data.get('ssn'):
                raise forms.ValidationError("SSN is required for Dual users.")
        return cleaned_data