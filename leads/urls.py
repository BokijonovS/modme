from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('leads', LeadViewSet)
router.register('expectations', ExpectationViewSet)
router.register('sets', SetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
