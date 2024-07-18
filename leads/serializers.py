from rest_framework import serializers
from .models import Lead, Expectation, Set


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class ExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expectation
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
