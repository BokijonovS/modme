from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.


GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
]


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='media/employees/')


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='media/teachers')


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField()
    additional_contacts = models.CharField(max_length=200)
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
    course_id = models.CharField(max_length=20)
    duration_h = models.TimeField()
    duration_m = models.IntegerField(help_text='Bu yerda kurs davomiyligi necha oy bolishi kiritiladi')
    price = models.IntegerField(help_text='Kurs narxi uzs da')
    description = models.TextField()


class Room(models.Model):
    name = models.CharField(max_length=30)



