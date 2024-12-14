from django.shortcuts import render, redirect
from .forms import InvestorAuthUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponseForbidden

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
            if user.role == 'Investor':
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
    
    return render(request, 'register.html', {'register_form': register_form})

@login_required
def investors(request):
    if request.user.role != 'Investor':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'investor.html')

# Developer Dashboard View
@login_required
def developers(request):
    if request.user.role != 'Developer':
        return HttpResponseForbidden("You are not authorized to view this page.")
    return render(request, 'developers.html')

# Dual Dashboard View
@login_required
def dual_dashboard(request):
    return render(request, 'base.html')