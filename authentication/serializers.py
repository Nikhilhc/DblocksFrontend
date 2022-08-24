from rest_framework import serializers
from .models import User,TeamLeader,TeamMember
from django.contrib import auth
from django.contrib.auth import login
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68,min_length=8,write_only=True)
    
    class Meta:
        model = User
        fields = ['email','username','password','role']
    
    def validate(self,attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        role = attrs.get('role','')
        if not role or role=='':
            raise serializers.ValidationError('Please specify the role of the user.')
        if not username.isalnum():
            raise serializers.ValidationError('The Username should only contain only alphanumeric characters.')
        return attrs

    
    def create(self,attrs):
        if attrs.get('role','')=='1':
            return User.objects.create_user(**attrs)
        if attrs.get('role','')=='2':
            return TeamLeader.objects.create_user(**attrs)
        if attrs.get('role','')=='3':
            return TeamMember.objects.create_user(**attrs)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,min_length=3,read_only=True)
    username = serializers.CharField(max_length=255,min_length=3)
    password = serializers.CharField(max_length=68,min_length=4,write_only=True)
    tokens = serializers.CharField(max_length=68,min_length=6,read_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','tokens']
