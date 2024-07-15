from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .emails import send_update_email
import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    phone = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='media/users/', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    username = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    history = HistoricalRecords()

    def __str__(self):
        return self.phone


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class DailyStudentStat(models.Model):
    date = models.DateField(unique=True)
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.date}"


class Update(models.Model):
    '''a model to get update informations from adminuser'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.created_at}'


@receiver(post_save, sender=Update)
def send_update_notification(sender, instance, created, **kwargs):
    '''a method to send a notification when a model is updated'''
    if created:
        users = User.objects.all()
        subject = f"New Update: {instance.title}"
        message = instance.content
        for user in users:
            send_update_email(user.email, subject, message)
