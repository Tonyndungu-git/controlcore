from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('weekly-challenges/', views.weekly_challenges, name='weekly_challenges'),
    path('contact/', views.contact_view, name='contact'),
]
