from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    office_details = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    times = models.TextField()
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student)

