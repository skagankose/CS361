from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    office_details = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):

        return str(self.first_name) +' ' + str(self.last_name)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):

        return str(self.first_name) + ' ' + str(self.last_name)

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    times = models.CharField(max_length=300, blank=True)
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student)

    def __unicode__(self):

        return self.name

