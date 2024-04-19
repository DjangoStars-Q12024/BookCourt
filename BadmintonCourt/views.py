from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import court, MBooking, NBooking, User
# Create your views here.
class HomeView(TemplateView):
    
    template_name = 'home.html'

class BookTableView(ListView):
    model = court
    template_name = 'booking/booking.html'

class MBookView(ListView):
    model = User
    template_name = 'booking/mbookingForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        court_id = self.request.GET.get('court_id')
        if court_id:
            court_object = court.objects.get(pk=court_id)
            context['court_name'] = court_object.courtName
        return context


class NBookView(TemplateView):
    template_name = 'booking/nbookingForm.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        court_id = self.request.GET.get('court_id')
        if court_id:
            court_object = court.objects.get(pk=court_id)
            context['court_name'] = court_object.courtName
        return context

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