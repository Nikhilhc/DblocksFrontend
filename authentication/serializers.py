from rest_framework import serializers
from .models import User,TeamLeader,TeamMember


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
    
