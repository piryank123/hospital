from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import ListView, View
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#Auth Views

def login(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('registration/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/appointments/loggedin/')
    else:

        return HttpResponseRedirect('/appointments/invalid/')

def loggedin(request):
    return render_to_response('registration/loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('registration/invalid_login.html')

def logout(request):
    auth.logout(request)

    return render_to_response('registration/logout.html')


