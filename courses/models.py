from django.db import models
from multiselectfield import MultiSelectField
from accounts.models import Teacher


class Group(models.Model):
    WEEKDAYS = (
        ('MO', 'Monday'),
        ('TU', 'Tuesday'),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday'),
    )

    name = models.CharField(max_length=50)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    days = MultiSelectField(choices=WEEKDAYS)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    lesson_start_time = models.TimeField()
    group_opened_time = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=70)
    course_id = models.CharField(max_length=20, null=True, blank=True)
    duration_h = models.TimeField()
    duration_m = models.IntegerField(help_text='Bu yerda kurs davomiyligi necha oy bolishi kiritiladi')
    price = models.IntegerField(help_text='Kurs narxi uzs da')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
