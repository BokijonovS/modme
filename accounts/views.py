from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from courses.models import Group
from .models import User, Student, Teacher, Update, DailyStat
from .serializers import (StudentSerializer, TeacherSerializer, UpdateSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     print(request)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class UpdateViewSet(ModelViewSet):
    '''This viewset does all the work on model Update and checks if the user is AdminUser'''
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class DailyStudentStatAPIView(APIView):
    def get(self, request, *args, **kwargs):
        last_stat = DailyStat.objects.all()
        if not last_stat:
            DailyStat.objects.create(
                date=timezone.now().date(),
                student_count=Student.objects.count(),
                group_count=Group.objects.count()
            )
            return Response({'message': 'created'}, status=status.HTTP_200_OK)
        else:
            last_stat = DailyStat.objects.latest('id')

        if last_stat.date == timezone.now().date():
            pass
        else:
            DailyStat.objects.create(
                date=timezone.now().date(),
                student_count=Student.objects.count(),
                group_count=Group.objects.count()
            )

            return Response({'message': 'done'}, status=status.HTTP_200_OK)
        return Response({'message': 'already done'}, status=status.HTTP_200_OK)
