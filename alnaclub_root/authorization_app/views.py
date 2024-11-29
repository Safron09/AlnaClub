from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import InvestorAuthUserCreationForm
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        register_form = InvestorAuthUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save() 
            return redirect('home')
    else:       
        register_form = InvestorAuthUserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})
