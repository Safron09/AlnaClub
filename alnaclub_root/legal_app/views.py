from django.shortcuts import render

# Create your views here.
def terms_of_service(request):
    return render(request, 'legal_app/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'legal_app/privacy_policy.html')