from django.contrib import admin
from django.urls import path
from .views import SignUpView, CustomLogoutView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('custom_logout/', CustomLogoutView.as_view(), name='custom_logout'),
]
