from rest_framework import serializers
from .models import User, Teacher, Student, Update, GraduatedStudent, DailyStat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'password' ]


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = ['id', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        teacher1 = Teacher.objects.create(user=user)
        return teacher1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['phone', 'first_name', 'password' ]


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
