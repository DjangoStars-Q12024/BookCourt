from django.urls import path
from .views import HomeView
from .import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('booking/', views.add_court, name='booking'),
]