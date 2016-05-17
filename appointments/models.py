from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Physician(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #physician = models.IntegerField(unique = True)
    #is_active = models.IntegerField(default = 1)
    def __str__(self):
        return self.user.first_name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #patient = models.IntegerField(unique = True)
    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    physician = models.OneToOneField(Physician, unique = False)
    patient = models.OneToOneField(Patient, unique = False)
    time = models.DateTimeField('datetime')
    status = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.time)
