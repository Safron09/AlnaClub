from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

# def developers(request):
#     return render(request, 'developers.html')

# def investors(request):
#     return render(request, 'investors.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

def faq(request):
    return render(request, 'faq.html')

# def signup(request):
#     return render(request, 'signup.html')

# def login(request):
#     return render(request, 'login.html')

# def our_story(request):
#     return render(request, 'our_story.html')

# def team(request):
#     return render(request, 'team.html')

# def contact_us(request):
#     return render(request, 'contact_us.html')

# def terms_of_service(request):
#     return render(request, 'terms_of_service.html')

# def privacy_policy(request):
#     return render(request, 'privacy_policy.html')