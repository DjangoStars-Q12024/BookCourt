from django.contrib import admin
from .models import court, MBooking, NBooking
# Register your models here.
admin.site.register(court)
admin.site.register(MBooking)
admin.site.register(NBooking)