from django.contrib import admin
from django.contrib.auth.models import User

from .models import Physician, Patient, Appointment
# Register your models here.

admin.site.register(Physician)
admin.site.register(Patient)
admin.site.register(Appointment)

