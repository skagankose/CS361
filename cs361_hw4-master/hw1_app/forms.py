from django import forms
from models import *

class TeacherForm(forms.Form):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    office_details = forms.CharField(max_length=300)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()

class StudentForm(forms.Form):

    # class Meta:
    #     model = Student
    #     fields = ('first_name', 'last_name', 'email')

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()


class CourseForm(forms.Form):

    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=20)
    classroom = forms.CharField(max_length=20)
    times = forms.CharField(max_length=300)
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

class enrollForm(forms.Form):

    students = forms.ModelChoiceField(queryset=Student.objects.all())
    courses = forms.ModelChoiceField(queryset=Course.objects.all())
