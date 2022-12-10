from rest_framework.viewsets import ModelViewSet
from .models import user_mobile
from .serializers import Otp_serializer, Register, User

class Register(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Register
