from django.conf.urls import url

from .views.patient_views import PatientsListView, PatientView
from .views.physician_views import PhysiciansListView, PhysicianView
from .views.appointment_views import AppointmentsListView, AppointmentView, MainView
from .views.user_views import login, auth_view, logout, loggedin, invalid_login

app_name = 'appointments'
urlpatterns = [
        url(r'^$',MainView.as_view(), name='main'),

        url(r'^patients/$', PatientsListView.as_view(), name='patient_list'),
        url(r'^new_patient/$', PatientView.as_view(), name='patient_new'),

        url(r'^physicians/$', PhysiciansListView.as_view(), name='physician_list'),
        url(r'^new_physician/$', PhysicianView.as_view(), name='physician_new'),

        url(r'^appointments/$', AppointmentsListView.as_view(), name='appointment_list'),
        url(r'^new_appointment/$', AppointmentView.as_view(), name='appointment_new'),

        url(r'^login/$',  login, name='login'),
        url(r'^auth/$',  auth_view, name='auth_view'),
        url(r'^logout/$', logout, name='logout'),
        url(r'^loggedin/$', loggedin, name='loggedin'),
        url(r'^invalid/$', invalid_login, name='invalid_login'),

]
