from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import CourtForm
# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

def booking(request):

    return render(request, 'booking.html')

def add_court(request):
    if request.method =="POST":
        form = CourtForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
    else:
        form = CourtForm()
    return render(request, 'booking.html',{'form':form})
