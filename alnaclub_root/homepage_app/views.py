from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscriber


def home(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'homepage_app/homepage.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

def faq(request):
    return render(request, 'faq.html')

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():  # Check for duplicate email
                Subscriber.objects.create(email=email)
                return render(request, 'homepage_app/homepage.html', {
                    'message': 'Subscription successful!',
                    'message_type': 'success'
                })
            else:
                return render(request, 'homepage_app/homepage.html', {
                    'message': 'This email is already subscribed.',
                    'message_type': 'error'
                })
        else:
            return render(request, 'homepage_app/homepage.html', {
                'message': 'Invalid email. Please try again.',
                'message_type': 'error'
            })

    return render(request, 'homepage_app/homepage.html')

def home(request):
    reviews = []  # Initialize an empty list for reviews
    with open('reviews.txt', 'r') as file:
        for line in file:
            text, source = line.rsplit('-', 1)  # Split each line into text and source (e.g., "Review text - John Doe")
            reviews.append({'text': text.strip('" '), 'source': source.strip()})  # Add review dict to the list

    context = {
        'reviews': reviews,  # Pass reviews to the template
    }
    return render(request, 'homepage_app/homepage.html', context)