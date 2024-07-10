from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from .models import User, Student, Teacher
from .serializers import (StudentSerializer, TeacherSerializer)


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
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]

    #def create(self, request, *args, **kwargs):



class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]
