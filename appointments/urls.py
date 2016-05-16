
from django.conf.urls import url
from . import views

app_name = 'appointment'
urlpatterns = [
        url(r'^$', views.PatientView.as_view(), name='patient_list')
        ]
