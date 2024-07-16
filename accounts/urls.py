from django.urls import path, include

from rest_framework import routers
from .views import UserViewSet, TeacherViewSet, StudentViewSet, UpdateViewSet, DailyStudentStatAPIView, StatsAPIView

'''here i used DefaultRouter to deal with all the things with urls'''
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('updates', UpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats-refresh/', DailyStudentStatAPIView.as_view()),
    path('stats/', StatsAPIView.as_view(), name='stats'),
]
