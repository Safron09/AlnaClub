from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import InvestorAuthUser

class InvestorAuthUserCreationForm(UserCreationForm):
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(required=False)  # Optional
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    occupation = forms.CharField(required=False)  # Optional
    ready_to_invest = forms.DecimalField(required=True, max_digits=12, decimal_places=2)
    return_goals = forms.CharField(widget=forms.Textarea, required=False)  # Optional

    class Meta:
        model = InvestorAuthUser
        fields = [
            'username', 'name', 'last_name', 'company_name', 'email',
            'phone_number', 'address', 'password1', 'password2', 'occupation',
            'ready_to_invest', 'return_goals',
        ]
