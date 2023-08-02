from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)


class Bus(models.Model):
    plate_number = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=100)
    seats = models.IntegerField()


class Trip(models.Model):
    NORMAL = 'Normal'
    EXPRESS = 'Express'

    TRIP_TYPE_CHOICES = [
        (NORMAL, 'Normal'),
        (EXPRESS, 'Express'),
    ]

    start_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_trips')
    end_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_trips')
    trip_type = models.CharField(max_length=10, choices=TRIP_TYPE_CHOICES, default=NORMAL)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats = models.IntegerField()
    paid = models.BooleanField(default=False)
