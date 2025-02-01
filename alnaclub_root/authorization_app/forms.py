from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from .models import InvestorAuthUser

class InvestorAuthUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('', 'Select Role'),
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
    ready_to_invest = forms.DecimalField(required=False, max_digits=12, decimal_places=2)
    return_goals = forms.CharField(widget=forms.Textarea, required=False)  # Optional
    projects_done = forms.IntegerField(required=False)
    ssn = forms.CharField(required=False)

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

    # Role-specific validations
    if role == '':
        self.add_error('role', "Please select a valid role.")
    elif role == 'Investor':
        if not cleaned_data.get('ready_to_invest') or not cleaned_data.get('return_goals'):
            self.add_error('ready_to_invest', "This field is required for Investors.")
            self.add_error('return_goals', "This field is required for Investors.")
    elif role == 'Developer':
        if not cleaned_data.get('projects_done'):
            self.add_error('projects_done', "This field is required for Developers.")
    elif role == 'Dual':
        if not cleaned_data.get('ssn'):
            self.add_error('ssn', "This field is required for Dual users.")

    return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Debugging output
        print(f"Debug: User - {user.username}, Superuser - {user.is_superuser}, Role - {getattr(user, 'role', None)}")

        # Allow SuperAdmins unconditionally
        if user.is_superuser:
            return

        # Allow users with valid roles
        if user.role in ['Investor', 'Developer', 'Dual']:
            return

        # Deny users without valid roles
        raise ValidationError(
            "Your account does not have a valid role. Please contact support.",
            code='invalid_login'
        )
