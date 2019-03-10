from django.conf.urls import url
from verifications import views

urlpatterns = [
    # ^sms_codes/(?P<mobile>1[3-9]\d{9})/$
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
]