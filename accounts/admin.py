from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *





admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
