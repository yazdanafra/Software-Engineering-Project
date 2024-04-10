from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class StudentProfessor(models.Model) :
    students = models.ForeignKey('Student', on_delete=models.CASCADE)
    professors = models.ForeignKey('Professor', on_delete=models.CASCADE)

class Professor(AbstractUser) :
    first_name = models.CharField(verbose_name="First Name", max_length=25, blank=False, default='')
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=False, default='')
    email = models.EmailField(unique=True, blank=False, null=False)
    national_no = models.CharField(verbose_name="National Number", max_length=10, unique=True, blank=False)
    sts = models.ManyToManyField('Student', verbose_name="students", through='StudentProfessor', related_name='professors')
    user_permissions = models.ManyToManyField(Permission, related_name='professors_permissions')
    groups = models.ManyToManyField(Group, related_name='professors_groups')
    

class Student(AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=25, blank=False, default='')
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=False, default='')
    stu_no = models.CharField(verbose_name="Student Number", max_length=10, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=True)
    pros = models.ManyToManyField('Professor', verbose_name="professors", through='StudentProfessor', related_name='students')
    user_permissions = models.ManyToManyField(Permission, related_name='students_permissions')
    groups = models.ManyToManyField(Group, related_name='students_groups')
    is_ta = models.BooleanField(default=False)
    phone_no = models.IntegerField(verbose_name="Phone Number", blank=False, null=False)