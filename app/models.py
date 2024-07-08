from django.contrib.auth.models import User
from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
]


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='media/employees/', null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='media/teachers', null=True, blank=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    additional_contacts = models.CharField(max_length=200, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)


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


class Course(models.Model):
    name = models.CharField(max_length=70)
    course_id = models.CharField(max_length=20, null=True, blank=True)
    duration_h = models.TimeField()
    duration_m = models.IntegerField(help_text='Bu yerda kurs davomiyligi necha oy bolishi kiritiladi')
    price = models.IntegerField(help_text='Kurs narxi uzs da')
    description = models.TextField(null=True, blank=True)


class Room(models.Model):
    name = models.CharField(max_length=30)




