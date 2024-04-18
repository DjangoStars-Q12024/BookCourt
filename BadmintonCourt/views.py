from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

def booking(request):

    return render(request, 'booking.html')

class MBookView(TemplateView):
    template_name = 'mbookingForm.html'

class NBookView(TemplateView):
    template_name = 'nbookingForm.html'

class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'useraccount.html'
    login_url = 'accounts/login/'

