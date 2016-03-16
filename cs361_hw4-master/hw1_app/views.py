from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, render
from forms import *

# Add Teacher and redirect success page
# START
def add_teacher(request):

    if request.method == 'POST':

        form = TeacherForm(request.POST)
        if form.is_valid():
            new_teacher = Teacher(first_name=request.POST['first_name'],
                                  last_name=request.POST['last_name'],
                                  office_details=request.POST['office_details'],
                                  phone=request.POST['email'],
                                  email=request.POST['email'])
            new_teacher.save()
            return HttpResponseRedirect('/all_teachers/')

    else:

        form = TeacherForm()

    return render_to_response('add_teacher.html', {'form': form}, RequestContext(request))

def all_teachers(request):

    teacher_list = Teacher.objects.all()
    return render_to_response('all_teachers.html', {'teacher_list': teacher_list, }, RequestContext(request))
# END

# Add Student and redirect success page
# START
def add_student(request):

    # print dict(request.POST)

    if request.method == 'POST':

        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student(first_name=request.POST['first_name'],
                                  last_name=request.POST['last_name'],
                                  email=request.POST['email'])
            new_student.save()
            return HttpResponseRedirect('/all_students/')

    else:

        form = StudentForm()

    return render(request,'add_student.html', {'form': form})

def all_students(request):

    student_list = Student.objects.all()
    return render_to_response('all_students.html', {'student_list': student_list, }, RequestContext(request))
# END

# Add Student and redirect success page
# START
def add_course(request):

    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():

            t = Teacher.objects.get(pk=request.POST['teacher'])

            new_course = Course(name=request.POST['name'],
                                code=request.POST['code'],
                                classroom=request.POST['classroom'],
                                times=request.POST['times'],
                                teacher=t,)


            new_course.save()

            students = dict(request.POST.lists())['students']
            for student in students:
                new_course.students.add(student)

            new_course.save()

            return HttpResponseRedirect('/all_courses/')

    else:

        form = CourseForm()

    return render_to_response('add_course.html', {'form': form}, RequestContext(request))

def all_courses(request):

    course_list = Course.objects.all()
    return render_to_response('all_courses.html', {'course_list': course_list, }, RequestContext(request))
# END

# Enroll a student into a course
# START
def enroll(request):

    if request.method == 'POST':

        form = enrollForm(request.POST)
        if form.is_valid():

            student = Student.objects.get(pk=request.POST['students'])
            course = Course.objects.get(pk=request.POST['courses'])
            course.students.add(student)
            course.save()

            enrolled_students = Student.objects.filter(course=course)
            return render_to_response('enrolled_students.html',
                                      {'enrolled_students': enrolled_students,
                                       'course': course,
                                       'student': student},
                                      RequestContext(request))

    else:

        form = enrollForm()

    return render_to_response('enroll.html', {'form': form}, RequestContext(request))
# END
