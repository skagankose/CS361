__author__ = 'k'

from django.conf.urls import url
from . import views

urlpatterns = [

    # Urls to add models via forms
    url(r'^add_teacher/$', views.add_teacher),
    url(r'^add_student/$', views.add_student),
    url(r'^add_course/$', views.add_course),

    # Success pages of forms
    url(r'^all_teachers/', views.all_teachers),
    url(r'^all_students/', views.all_students),
    url(r'^all_courses/', views.all_courses),

    # Enroll page
    url(r'^enroll/', views.enroll),

]