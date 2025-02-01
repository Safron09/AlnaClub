from django.shortcuts import render, redirect
from .forms import InvestorAuthUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from .decorators import role_required

def register(request):
    if request.method == "POST":
        register_form = InvestorAuthUserCreationForm(request.POST)
        
        # Check if form is valid and save the user
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.role = register_form.cleaned_data.get('role')  # Ensure role is set
            user.save()  # Save the user object to the database
            
            # Log the user in after registration
            login(request, user)
            
            # Redirect based on the user's role
            if user.is_superuser:
                return redirect('base')
            elif user.role == 'Investor':
                return redirect('investors')
            elif user.role == 'Developer':
                return redirect('developers')
            elif user.role == 'Dual':
                return redirect('home')
        else:
            # If form is invalid, display errors
            print("Form errors:", register_form.errors)

    else:
        register_form = InvestorAuthUserCreationForm()
    
    return render(request, 'auth/register.html', {'register_form': register_form})

@login_required
@role_required(allowed_roles=['Investor'])
def investors(request):
    if not request.user.is_superuser and request.user.role != 'Investor':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'investors_app/investor.html')

# Developer Dashboard View
@login_required
@role_required(allowed_roles=['Developer'])
def developers(request):
    if request.user.is_superuser: 
        return render(request, 'developers_app/developers.html')
    elif request.user.role == 'Developer': 
        return render(request, 'developers_app/developers.html')
    return HttpResponseForbidden("You are not authorized to view this page.") 

# Dual Dashboard View
@login_required
@role_required(allowed_roles=['Dual'])
def dual_dashboard(request):
    if not request.user.is_superuser and request.user.role != 'Dual':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'base.html')