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
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from appointments.models import Appointment
from appointments.forms import AppointmentForm

# Create your views here.

class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='appointments:login'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class MainView(LoginRequiredMixin, TemplateView):
    template_name = "appointments/main.html"


class AppointmentsListView(ListView):
    model = Appointment
    context_object_name = 'appointments'


class AppointmentViewOld(CreateView):
    model = Appointment
    success_url = reverse_lazy('appointment_list')
    fields = ['physician', 'patient', 'time','status']

class AppointmentView(View):
    def get(self,request):
        form = AppointmentForm()

        return render_to_response('registration/appointment.html',{'form':form,'name':'Appointment'}, RequestContext(request, {}))

    def post(self,request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print 1
            print form.cleaned_data['time']
            with transaction.atomic():
                appointment = Appointment.objects.create(
                        time = form.cleaned_data['time'],
                        status = form.cleaned_data['status'],
                        physician_id = form.cleaned_data['physician'],
                        patient_id = form.cleaned_data['patient'],
                        )
        else:
            print 2
        return HttpResponseRedirect('/appointments/')
