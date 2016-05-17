from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction

from .models import Physician, Patient, Appointment
from .forms import RegistrationForm
# Create your views here.

class MainView(TemplateView):
    template_name = "appointments/main.html"


class PatientView(ListView):
    model = Patient


class PatientCreate(View):
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            )
            with transaction.atomic():
                patient = Patient.objects.create(user_id = user.id)

        return HttpResponseRedirect('/appointments/patients/')
    def get(self,request):
        form = RegistrationForm()

        return render_to_response('registration/register.html',{'form':form,'name':'Patient'})


class PhysicianView(ListView):
    model = Physician


class PhysicianCreate(View):
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            )
            with transaction.atomic():
                physician = Physician.objects.create(user_id = user.id)

        return HttpResponseRedirect('/appointments/physicians/')
    def get(self,request):
        form = RegistrationForm()

        return render_to_response('registration/register.html',{'form':form,'name':'Physician'})


class AppointmentView(ListView):
    model = Appointment


class AppointmentCreate(CreateView):
    model = Appointment
    success_url = reverse_lazy('appointment_list')
    fields = ['physician', 'patient', 'time','status']
