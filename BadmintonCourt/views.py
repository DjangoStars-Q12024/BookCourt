from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
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

class UserAccountView(LoginRequiredMixin, ListView):
    model = MBooking
    template_name = 'useraccount.html'
    login_url = 'accounts/login/'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.groups.filter(name='Members').exists():
            queryset = queryset.filter(user=self.request.user)
        else:
            queryset = queryset.all()
        return queryset