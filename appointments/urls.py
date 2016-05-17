
from django.conf.urls import url
from .views.patient_views import PatientsListView, PatientView
from .views.physician_views import PhysiciansListView, PhysicianView
from .views.appointment_views import AppointmentsListView, AppointmentView, MainView

app_name = 'appointments'
urlpatterns = [
        url(r'^$', MainView.as_view(), name='main'),

        url(r'^patients/$', PatientsListView.as_view(), name='patient_list'),
        url(r'^new_patient$', PatientView.as_view(), name='patient_new'),

        url(r'^physicians/$', PhysiciansListView.as_view(), name='physician_list'),
        url(r'^new_physician/$', PhysicianView.as_view(), name='physician_new'),

        url(r'^appointments/$', AppointmentsListView.as_view(), name='appointment_list'),
        url(r'^new_appointment/$', AppointmentView.as_view(), name='appointment_new'),
]
