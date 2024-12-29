from django.shortcuts import render

def our_story(request):
    return render(request, 'company_app/our_story.html')

def team(request):
    return render(request, 'company_app/team.html')

def contact_us(request):
    return render(request, 'company_app/contact_us.html')