from django.conf.urls import url

from .views.patient_views import PatientsListView, PatientView
from .views.physician_views import PhysiciansListView, PhysicianView
from .views.appointment_views import AppointmentsListView, AppointmentView, MainView
from . import views

app_name = 'appointments'
urlpatterns = [
        url(r'^$',MainView.as_view(), name='main'),

        url(r'^patients/$', PatientsListView.as_view(), name='patient_list'),
        url(r'^new_patient/$', PatientView.as_view(), name='patient_new'),

        url(r'^physicians/$', PhysiciansListView.as_view(), name='physician_list'),
        url(r'^new_physician/$', PhysicianView.as_view(), name='physician_new'),

        url(r'^appointments/$', AppointmentsListView.as_view(), name='appointment_list'),
        url(r'^new_appointment/$', AppointmentView.as_view(), name='appointment_new'),

        url(r'^login/$',  views.login, name='login'),
        url(r'^auth/$',  views.auth_view, name='auth_view'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^loggedin/$', views.loggedin, name='loggedin'),
        url(r'^invalid/$', views.invalid_login, name='invalid_login'),

]
