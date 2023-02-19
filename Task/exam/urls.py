# from django.conf.urls import url
from django.urls import path, include
from .views import (
    CourseApiView,QuestionApiView,base,Question2,exam,examQuestion

)
urlpatterns = [
    path('api/course',CourseApiView.as_view(),name="course"),
    path('api/exam',QuestionApiView.as_view(),name="question"),
    path('api/exam/<str:name>/',QuestionApiView.as_view(),name="question2"),
    path("",base,name="coursePage"),
    path("question",Question2,name="questionPage"),
    path("exam",exam,name="examPage"),
    path("examQuestion",examQuestion,name="examQuestion")
]