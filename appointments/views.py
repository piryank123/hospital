from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Physician, Patient, Appointment
# Create your views here.

class PatientView(ListView):
    model = Patient

