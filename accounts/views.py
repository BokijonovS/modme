from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, status
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer, TeacherSerializer
from .groups import teacher_group


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(groups=teacher_group)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password("system_teacher")
        user.groups.add(teacher_group)
        user.save()
