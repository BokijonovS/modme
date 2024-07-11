from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeacherViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
