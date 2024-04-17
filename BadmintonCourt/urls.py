from django.urls import path
from .views import HomeView, MBookView, NBookView, UserAccountView
from .import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('booking/', views.booking, name='booking'),
    path('booking/mbook', MBookView.as_view(), name='mbook'),
    path('booking/nbook', NBookView.as_view(), name='nbook'),
    path('useraccount', UserAccountView.as_view(), name='useraccount'),
    
]