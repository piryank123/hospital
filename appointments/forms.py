import re

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django.forms import DateTimeField

from .models import Physician, Patient, Appointment

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Fist Name"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Last Name"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))


class AppointmentForm(forms.Form):
    physician_choices = [(physician.id, physician.user.first_name) for physician in Physician.objects.all()]
    patient_choices = [(patient.id, patient.user.first_name) for patient in Patient.objects.all()]
    physician = forms.ChoiceField(choices = physician_choices, label=_("Physician"), required = True)
    patient = forms.ChoiceField(choices = patient_choices, label=_("Patient"), required = True)
    #patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label=_("patient"))
    #physician = forms.ChoiceField(choices = Physician, label=_("physician"))
    #patient = forms.ChoiceField(choices = Patient, label=_("patient"))
    #time = forms.DateTimeField(input_formats=['%d-%m-%y %H:%M',])
    time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs=dict(required=True)), label=_("Time"))
    status = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Status"))
