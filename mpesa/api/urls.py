from django.urls import path, include
from mpesa.api.views import *
urlpatterns = [
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
]
