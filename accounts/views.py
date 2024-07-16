from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from courses.models import Group
from .models import User, Student, Teacher, Update, DailyStat, GraduatedStudent
from .utils import percentage_counter
from .serializers import (StudentSerializer, TeacherSerializer, UpdateSerializer, DailyStatSerializer,
                          GraduatedStudentSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name']
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Add the student to RemovedStudent before deleting
        GraduatedStudent.objects.create(student_name=instance.user.first_name)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']
    permission_classes = [permissions.IsAuthenticated]


class UpdateViewSet(ModelViewSet):
    '''This viewset does all the work on model Update and checks if the user is AdminUser'''
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class DailyStudentStatAPIView(APIView):
    serializer_class = DailyStatSerializer
    def get(self, request, *args, **kwargs):
        last_stat = DailyStat.objects.all()
        if not last_stat:
            DailyStat.objects.create(
                date=timezone.now().date(),
                student_count=Student.objects.count(),
                group_count=Group.objects.count(),
                graduated_count=GraduatedStudent.objects.count(),
            )
            return Response({'message': 'created'}, status=status.HTTP_200_OK)
        else:
            last_stat = DailyStat.objects.latest('id')

        if last_stat.date == "2024-07-20":
            pass
        else:
            DailyStat.objects.create(
                date="2024-07-20",
                student_count=Student.objects.count(),
                group_count=Group.objects.count(),
                graduated_count=GraduatedStudent.objects.count(),
            )

            return Response({'message': 'done'}, status=status.HTTP_200_OK)
        return Response({'message': 'already done'}, status=status.HTTP_200_OK)


class StatsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        graduated_students = GraduatedStudent.objects.all()
        graduated_serializer = GraduatedStudentSerializer(graduated_students, many=True)
        today = timezone.now().date()
        one_day_before = today - timedelta(days=-3)
        daily_stats = DailyStat.objects.filter(date=today)
        daily_stat_serializer = DailyStatSerializer(daily_stats, many=True)
        print(daily_stat_serializer.data)
        daily_stats1 = DailyStat.objects.filter(date=one_day_before)
        daily_stat_serializer1 = DailyStatSerializer(daily_stats1, many=True)
        print(daily_stat_serializer1.data)

        daily_stat1 = daily_stat_serializer.data
        daily_stat2 = daily_stat_serializer1.data
        student_difference = daily_stat1[0]['graduated_count'] - daily_stat2[0]['graduated_count']
        print(student_difference)
        print(percentage_counter(daily_stat1[0]['graduated_count'], daily_stat2[0]['graduated_count']))

        combined_data = {
            'graduated_students': graduated_serializer.data,
            'daily_stats': daily_stat_serializer.data,
            'yesterday_stats': daily_stat_serializer1.data,
        }

        return Response(combined_data)
