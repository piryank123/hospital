
from django.conf.urls import url
from . import views

app_name = 'appointments'
urlpatterns = [
        url(r'^$', views.MainView.as_view(), name='main'),
        url(r'^patients/$', views.PatientView.as_view(), name='patient_list'),
        url(r'^new_patient/$', views.PatientCreate.as_view(), name='patient_new'),
        url(r'^physicians/$', views.PhysicianView.as_view(), name='physician_list'),
        url(r'^new_physician/$', views.PhysicianCreate.as_view(), name='physician_new'),
        url(r'^appointments/$', views.AppointmentView.as_view(), name='appointment_list'),
        url(r'^new_appointment/$', views.AppointmentCreate.as_view(), name='appointment_new'),
]
