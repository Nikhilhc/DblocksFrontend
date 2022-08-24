from django.shortcuts import render
from django.http import Http404
from rest_framework import generics,status
from .serializers import CreateTeamSerializer, UpdateTaskSerializerMember
from .serializers import CreateTaskSerializer
from .serializers import UpdateTaskSerializerLeader
from .serializers import GetAllTaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .celery_tasks import send_mail_func
# Create your views here.


class CreateTeam(generics.GenericAPIView):
    
    serializer_class = CreateTeamSerializer

    def post(self,request):
        data = request.data
        if request.user.username=='':
            return Response({'ret':'Please login to proceed'},status=status.HTTP_401_UNAUTHORIZED)
        if request.user.role == '1':
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            return Response(user_data,status=status.HTTP_201_CREATED)
        else:
            return Response({'ret':'Only Users can create a team'},status=status.HTTP_201_CREATED)


class CreateTask(generics.GenericAPIView):
    
    serializer_class = CreateTaskSerializer

    def post(self,request):
        data = request.data
        if request.user.username=='':
            return Response({'ret':'Please login to proceed'},status=status.HTTP_401_UNAUTHORIZED)
        if request.user.role == '1':
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            team_leader_email = self.serializer_class.Meta.model.objects.get(id=serializer.data['id']).team.team_leader.email
            import ipdb;ipdb.set_trace()
            send_mail_func.delay(email=team_leader_email)
            return Response(user_data,status=status.HTTP_201_CREATED)
        else:
            return Response({'ret':'Only Users can create a team'},status=status.HTTP_201_CREATED)


class UpdateTask(APIView):

    serializer_class = UpdateTaskSerializerLeader
    def get_object(self,pk):
        try:
            return self.serializer_class.Meta.model.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if snippet.team.team_leader.username == request.user.username:
            serializer = self.serializer_class(snippet)
            return Response(serializer.data)
        else:
            serializer = UpdateTaskSerializerMember(snippet)
            return Response(serializer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        if request.user.username=='':
            return Response({'ret':'Please login to proceed'},status=status.HTTP_401_UNAUTHORIZED)
        serializer = UpdateTaskSerializerMember(data,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)


class GetAllTasksApi(APIView):

    serializer_class = GetAllTaskSerializer

    def get(self,request):
        
        print('sent')
        data =self.serializer_class.Meta.model.objects.all()
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data)