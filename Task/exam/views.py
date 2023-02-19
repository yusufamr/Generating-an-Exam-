from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Question
from .models import Course as C1

from .serializers import CourseSerializer
from .serializers import QuestionSerializer,ChapterSerializer

class CourseApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.data['id'])
            for i in range(1,serializer.data['noOfChapters']+1):
                serializer2 = ChapterSerializer(data={"ChapterNumber":i,"courseID":serializer.data['id']})
                if serializer2.is_valid() :
                    serializer2.save()
                    Response(serializer2.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
            return redirect("coursePage")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect("questionPage")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,name):
        questions=Question.objects.filter(courseID=C1.objects.get(name=name).id)
        Q=QuestionSerializer(questions,many=True)
        return render(request,"examQuestion.html",{'ques':Q.data})
        
def  base(request):
    return render(request,"base.html")
def  Question2(request):
    return render(request,"newpage.html")
def exam(request):
    return render(request,"exam.html",{'courses': C1.objects.all() })
def examQuestion(request):
    return render(request,"examQuestion.html")