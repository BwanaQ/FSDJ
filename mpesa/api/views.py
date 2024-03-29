from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from mpesa.models import LNMOnline
from mpesa.api.serializers import LNMOnlineSerializer
class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(f"This is request.data {request.data}")