from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import logout

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(TemplateView):
    template_name = 'registration/logout.html'

    def post(self, request):
        logout(request)
        return redirect('custom_logout')