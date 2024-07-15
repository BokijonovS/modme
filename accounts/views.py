from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from .models import User, Student, Teacher, Update
from .serializers import (StudentSerializer, TeacherSerializer, UpdateSerializer)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .utils import calculate_daily_change


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request)


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


class StudentStatsView(APIView):
    permission_classes = [IsAdminUser]  # Optional, restrict access to admin users

    def get(self, request):
        daily_change = calculate_daily_change()
        return Response({'daily_change': daily_change})
