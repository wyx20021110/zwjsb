from django.urls import path
from .views import *
app_name = 'course'
urlpatterns = [
    path('', CourseIndex.as_view(), name='course_index'),
    path('<str:name>/',CourseDetail.as_view()),


]