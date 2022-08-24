from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Team,Task


class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','team_leader','team_members']
    
    def validate(self,attrs):
        name = attrs.get('name','')
        team_members = attrs.get('team_members','')
        if not name or name == '':
            raise serializers.ValidationError('Please enter name of the Team')
        if not team_members or team_members==[] or team_members=='':
            raise serializers.ValidationError('Please select members for the team')
        return attrs
    

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','team']
    
    def validate(self,attrs):
        name = attrs.get('name','')
        team = attrs.get('team','')
        if not name or name == '':
            raise serializers.ValidationError('Please enter name of the Team')
        if not team or team==[] or team=='':
            raise serializers.ValidationError('Please select a team')
        return attrs


class UpdateTaskSerializerLeader(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name','team','status','completed_at']


class UpdateTaskSerializerMember(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']


class GetAllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','team','status','completed_at','started_at']