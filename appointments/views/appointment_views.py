from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.views.decorators.csrf import csrf_protect

from appointments.models import Appointment

# Create your views here.

class MainView(TemplateView):
    template_name = "appointments/main.html"

class AppointmentsListView(ListView):
    model = Appointment
    context_object_name = 'appointments'


class AppointmentView(CreateView):
    model = Appointment
    success_url = reverse_lazy('appointment_list')
    fields = ['physician', 'patient', 'time','status']


#TODO: Implement AppointmentView by inheriting View (get, post)
#TODO: use forms.py to create form
