from django.shortcuts import render, redirect
from .forms import InvestorAuthUserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        register_form = InvestorAuthUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.role = register_form.cleaned_data.get('role')
            user.save()
            login(request, user)
            if user.role == 'Investor':
                return redirect('investor_dashboard')
            elif user.role == 'Developer':
                return redirect('developer_dashboard')
            elif user.role == 'Dual':
                return redirect('dual_dashboard')
    else:
        register_form = InvestorAuthUserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})