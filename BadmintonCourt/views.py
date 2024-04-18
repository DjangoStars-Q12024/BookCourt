from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import court, MBooking, NBooking
# Create your views here.
class HomeView(TemplateView):
    
    template_name = 'home.html'

class BookTableView(ListView):
    model = court
    template_name = 'booking.html'

class MBookView(TemplateView):
    template_name = 'mbookingForm.html'

class NBookView(TemplateView):
    template_name = 'nbookingForm.html'

class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'useraccount.html'
    login_url = 'accounts/login/'