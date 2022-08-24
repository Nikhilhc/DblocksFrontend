from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.views import APIView
from django.contrib.auth import login,logout
from rest_framework import permissions
from authentication.models import User
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.


class RegisterAPIView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.username!='':
            return Response({'ret':'Please logout to login as a different user.'},status=status.HTTP_200_OK)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        login(request,user)
        return Response({'ret':user.tokens()},status=status.HTTP_200_OK)


class Logout(APIView):
    def post(self, request, format=None):
        # simply delete the token to force a login
        refresh_token = request.user.tokens()['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        logout(request)
        return Response(status=status.HTTP_200_OK)

