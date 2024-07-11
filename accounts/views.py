from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, status
from rest_framework.viewsets import ModelViewSet

from .models import User, Student, Teacher, Update
from .serializers import (StudentSerializer, TeacherSerializer, UpdateSerializer)
from .models import User
from .serializers import UserSerializer, TeacherSerializer
from .groups import teacher_group


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateViewSet(ModelViewSet):
    '''This viewset does all the work on model Update and checks if the user is AdminUser'''
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    def get_queryset(self):
        return User.objects.filter(groups=teacher_group)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password("system_teacher")
        user.groups.add(teacher_group)
        user.save()
