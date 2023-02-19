from rest_framework import serializers

from .models import Question
from .models import Course,Chapter

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name','noOfChapters')

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id','ChapterNumber','courseID')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question','correctChoice','wrongChoice1','wrongChoice2','difficulty','objective','courseID','chapterNo')