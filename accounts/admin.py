from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *


@admin.register(User)
class UserAdmin(SimpleHistoryAdmin):
    list_display = ('phone', 'role', 'birth_date', 'gender', 'photo')


@admin.register(Teacher)
class TeacherAdmin(SimpleHistoryAdmin):
    list_display = ('phone', 'role', 'birth_date', 'gender', 'photo')


@admin.register(Student)
class StudentAdmin(SimpleHistoryAdmin):
    list_display = ('phone', 'role', 'birth_date', 'gender', 'photo')
