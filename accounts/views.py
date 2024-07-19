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

        dailystat = DailyStat.objects.create(
                date=timezone.now().date(),
                student_count=Student.objects.count(),
                group_count=Group.objects.count(),
                graduated_count=GraduatedStudent.objects.count(),
            )

        return Response({'message': 'done'}, status=status.HTTP_200_OK)


class StatsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_day_before = today - timedelta(days=1)

        daily_stats = DailyStat.objects.filter(date=today)
        daily_stat_serializer = DailyStatSerializer(daily_stats, many=True)

        daily_stats1 = DailyStat.objects.filter(date=one_day_before)
        daily_stat_serializer1 = DailyStatSerializer(daily_stats1, many=True)

        today = daily_stat_serializer.data
        yesterday = daily_stat_serializer1.data
        print(today[-1])
        print(yesterday[-1])
        stats = {}
        if today:
            if yesterday:
                if yesterday[-1]['graduated_count'] != 0:
                    graduated_difference = percentage_counter(
                        today[-1]['graduated_count'],
                        yesterday[-1]['graduated_count']
                    )
                    stats['graduated'] = graduated_difference
                else:
                    graduated_difference = today[-1]['graduated_count'] - yesterday[-1]['graduated_count']
                    stats['graduated'] = graduated_difference

                if yesterday[-1]['student_count'] != 0:
                    student_difference = percentage_counter(
                        today[-1]['student_count'],
                        yesterday[-1]['student_count']
                    )
                    stats['student'] = student_difference
                else:
                    student_difference = today[-1]['student_count'] - yesterday[-1]['student_count']
                    stats['student'] = student_difference

                if yesterday[-1]['group_count'] != 0:
                    group_difference = percentage_counter(
                        today[-1]['group_count'],
                        yesterday[-1]['group_count']
                    )
                    stats['group'] = group_difference
                else:
                    group_difference = today[-1]['group_count'] - yesterday[-1]['group_count']
                    stats['group'] = group_difference
            else:
                graduated_difference = today[-1]['graduated_count']
                student_difference = today[-1]['student_count']
                group_difference = today[-1]['group_count']

                stats['graduated'] = graduated_difference
                stats['student'] = student_difference
                stats['group'] = group_difference
        else:
            stats['graduated'] = 0
            stats['student'] = 0
            stats['group'] = 0

        combined_data = {
            'graduated_students': stats['graduated'],
            'student_stats': stats['student'],
            'group_stats': stats['group'],
        }

        return Response(combined_data)
