from django.contrib.admin import site
from hw1_app.models import Course, Student, Teacher

site.register(Course)
site.register(Student)
site.register(Teacher)
