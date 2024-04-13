from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class court(models.Model):
    courtName = models.TextField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    amount = models.FloatField()
    available = models.BooleanField(default=True)

class MBooking(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='member',
        limit_choices_to={'groups__name': 'Members'}
    )
    court = models.OneToOneField(
        court, 
        on_delete=models.CASCADE, 
        related_name='Mcourt',
    )
    def save(self, *args, **kwargs):
        self.court.available = False  # Set the court as unavailable when a booking is made
        self.court.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.court.available = True  # Set the court as available when a booking is cancelled
        self.court.save()
        super().delete(*args, **kwargs)

class NBooking(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.EmailField()
    court = models.OneToOneField(
        court, 
        on_delete=models.CASCADE, 
        related_name='Ncourt',
    )
    def save(self, *args, **kwargs):
        self.court.available = False  # Set the court as unavailable when a booking is made
        self.court.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.court.available = True  # Set the court as available when a booking is cancelsled
        self.court.save()
        super().delete(*args, **kwargs)