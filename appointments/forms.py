import re

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm

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

