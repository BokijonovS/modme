from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from .models import User, Student, Teacher, Update, DailyStudentStat
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


def index(request):
    last_stat = DailyStudentStat.objects.last()

    if not last_stat or last_stat.date != timezone.now().date():
        # Create a new DailyStudentStat entry for today
        DailyStudentStat.objects.create(
            date=timezone.now().date(),
            total_count=Student.objects.count()
        )

    return HttpResponse('done', status=200)
