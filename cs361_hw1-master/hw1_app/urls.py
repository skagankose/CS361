__author__ = 'k'

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^histogram/([-\w]+)/', views.histogram_function_error),
    url(r'^histogram/([-\w]+).([-\w]+)/', views.histogram_function),

]