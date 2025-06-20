from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')



def weekly_challenges(request):
    # Titles and descriptions for each challenge
    challenge_data = [
        {
            "title": "Elevator Position Control with Tab Memory & State Machine",
            "description": [
                "Multi-floor logic",
                "Priority-based floor requests",
                "Tab memory for persistence"
            ],
            "github_url": "https://github.com/Tonyndungu-git/controlcore/tree/main/codesys_challenges/01_elevator_tab_memory",
            "completed": True,
        },
        {
            "title": "Automated Conveyor Sorting System with Vision Sensor Integration (Mock Data)",
            "description": [
                "Sorting logic based on \"sensor\" input",
                "Diverter control using timers",
                "Simulation of color/size sorting"
            ],
            "completed": False,
        },
        {
            "title": "PID-Controlled Thermal Chamber with Auto-Tuning & Data Logging",
            "description": [
                "Two PID zones: heating and cooling",
                "Auto-tune simulation",
                "CSV or SD card export of logs"
            ],
            "completed": False,
        },
        {
            "title": "SCADA-Controlled Water Distribution with Pressure, Leak, and Valve Control",
            "description": [
                "Leak detection from abnormal flow rates",
                "Pressure sensor simulation",
                "HMI visualization panel"
            ],
            "completed": False,
        },
        {
            "title": "Robotic Arm 3-Axis Control with Manual/Auto Mode + Safety Interlock",
            "description": [
                "Jog mode and automated sequence",
                "Axis position logic",
                "Limit switch simulation and E-Stop logic"
            ],
            "completed": False,
        },
        {
            "title": "Smart Warehouse AGV Navigation with RFID and Obstacle Logic",
            "description": [
                "RFID tag route selection",
                "Obstacle simulation with timers",
                "Autonomous path selection using logic blocks"
            ],
            "completed": False,
        },
        {
            "title": "Energy Monitoring & Load Shedding System (Power Factor & Demand Limits)",
            "description": [
                "Simulated real-time power measurements",
                "Priority-based load shedding",
                "Reactive compensation strategy"
            ],
            "completed": False,
        },
        {
            "title": "MQTT-Based Distributed Valve Control (Edge PLC + Central Monitor)",
            "description": [
                "Multiple simulated devices over MQTT",
                "Central SCADA-like controller",
                "Offline timeout alerts"
            ],
            "completed": False,
        },
        {
            "title": "Packaging Line Fault Recovery using Sequential Function Chart (SFC)",
            "description": [
                "Conveyor jam simulation and auto-retry",
                "Step-based SFC with transitions",
                "Alarm reset and manual override mode"
            ],
            "completed": False,
        },
        {
            "title": "Redundant Pump Control with Auto Alternation + Failover",
            "description": [
                "Two-pump setup with alternation logic",
                "Fault detection and switch to backup",
                "Runtime balancing and alarm notifications"
            ],
            "completed": False,
        },
    ]

    return render(request, 'weekly_challenges.html', {"challenges": challenge_data})

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
