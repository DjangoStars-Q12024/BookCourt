from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class court(models.Model):
    courtName = models.TextField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    amount = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.courtName


class MBooking(models.Model):
    user = models.ForeignKey(
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
    def __str__(self):
        return f"{self.user.first_name} - {self.court}"

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
        self.court.available = True  # Set the court as available when a booking is cancelled
        self.court.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.firstName