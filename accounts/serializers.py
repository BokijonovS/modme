from rest_framework import serializers
from .models import Teacher, Student, Update, GraduatedStudent, DailyStat


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


class GraduatedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduatedStudent
        fields = '__all__'


class DailyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStat
        fields = '__all__'
