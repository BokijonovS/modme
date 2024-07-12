from rest_framework import serializers
from .models import Teacher, Student, Update


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    '''serializer for model Update'''
    class Meta:
        model = Update
        fields = '__all__'
