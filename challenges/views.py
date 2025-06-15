from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def challenges_view(request):
    return render(request, 'challenges.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        message = request.POST.get('contact_message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject="New Contact Message - ControlCore",
            message=full_message,
            from_email='your-email@example.com',
            recipient_list=['your-email@example.com'],  # Update this
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('contact'))

    return render(request, 'contact.html')
