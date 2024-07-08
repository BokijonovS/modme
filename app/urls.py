from django.urls import path, include

from rest_framework import routers
from .views import EmployeeViewSet, TeacherViewSet, StudentViewSet, GroupViewSet, CourseViewSet, RoomViewSet

'''here i used DfaultRouter to deal with all the things with urls'''
router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('groups', GroupViewSet)
router.register('courses', CourseViewSet)
router.register('rooms', RoomViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
