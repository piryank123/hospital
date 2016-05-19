from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import ListView, View
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db import transaction
from django.views.decorators.csrf import csrf_protect

from appointments.models import Patient
from appointments.forms import RegistrationForm

# Patient Views

class PatientsListView(ListView):
    model = Patient
    context_object_name = 'patients'


class PatientView(View):
    def get(self,request):
        form = RegistrationForm()

        return render_to_response('registration/register.html',{'form':form,'name':'Patient'}, RequestContext(request, {}))

    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    email = form.cleaned_data['email'],
                    )
                patient = Patient.objects.create(user_id = user.id)

        return HttpResponseRedirect('/patients/')

