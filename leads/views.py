from django.shortcuts import render
from rest_framework import viewsets

from .models import Lead, Expectation, Set
from .serializers import *


# Create your views here.


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class ExpectationViewSet(viewsets.ModelViewSet):
    queryset = Expectation.objects.all()
    serializer_class = ExpectationSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

