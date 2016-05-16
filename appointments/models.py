from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Physician(models.Model):
    physician_id = models.OneToOneField(User, unique = True)
    is_active = models.IntegerField(default = 1)


class Patient(models.Model):
    patient_id = models.OneToOneField(User, unique = True)


class Appointment(models.Model):
    physician_id = models.OneToOneField(Physician)
    patient_id = models.OneToOneField(Patient)
    time = models.DateTimeField('datetime')
    status = models.CharField(max_length = 20)


