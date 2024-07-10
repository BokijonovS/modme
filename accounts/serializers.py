from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', "last_name", 'phone', 'photo', 'birth_date', 'gender', 'groups']


class TeacherSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='teacher-detail')
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', "last_name", 'phone', 'photo', 'birth_date', 'gender', 'groups']
        read_only_fields = ['groups']

