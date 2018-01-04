from django.conf.urls import url
from . import views
app_name = 'myform'

urlpatterns = [
    url(r'^check/', views.CreateForm, name='CreateForm'),
    url(r'^phone_check/', views.VerifiedPhone, name='VerifiedPhone'),
    url(r'^sms/', views.SmsSend, name='SmsSend'),
]
