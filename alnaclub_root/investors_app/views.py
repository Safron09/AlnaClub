from django.shortcuts import render

# Create your views here.
def investors(request):
    return render(request, 'investors_app/investors.html') 