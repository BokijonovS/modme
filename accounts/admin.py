from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *


@admin.register(User)
class UserAdmin(SimpleHistoryAdmin):
    list_display = ('phone', 'birth_date', 'gender', 'photo')


admin.site.register(Teacher)
admin.site.register(Student)
