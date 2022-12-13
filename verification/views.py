from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import user_mobile
from .serializers import Otp_serializer, Register, User, Otp_verifier
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .helper import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import CreateAPIView

class Register(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Register
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'})
        login(request, user)
        token, li = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class Otp_checker(CreateAPIView):
    
    serializer_class = Otp_verifier
    permission_classes = [AllowAny]

    def post(self, serializer):
        
        user = User.objects.get(username = self.request.data['username'])
        print(user.password)
        user.set_password(raw_password = user.password)
        user.save
        otp_owner = user_mobile.objects.get(user = user.pk)
        if otp_owner.isVerified == True:
            print('------+++++++++++++++++++++++------------------------')
            return Response({'details':'alredy verifide accout'}, status=status.HTTP_200_OK)
        given_otp = otp_owner.counter
        recived = self.request.data['recived_otp']
        if int(given_otp) == int(recived):
            otp_owner.recived_otp = recived
            otp_owner.isVerified = True
            otp_owner.save()
            print('otp ckecked done')
            obj = Sucessmassage(str(otp_owner.Mobile))
            obj.send_otp_via_message()
            owner = authenticate(username = user.username, password = user.password)
            print(owner)
            login(self.request, user)
            token, li = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})