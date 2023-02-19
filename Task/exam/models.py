from django.db import models

# Create your models here.
class  Course(models.Model):
    name = models.CharField(max_length=15)
    noOfChapters=models.IntegerField()

class Chapter(models.Model):
    ChapterNumber = models.IntegerField()
    courseID = models.ForeignKey(Course,on_delete=models.CASCADE)

class Question(models.Model):
    question = models.CharField(max_length=50)
    correctChoice = models.CharField(max_length=50)
    wrongChoice1 = models.CharField(max_length=50)
    wrongChoice2 = models.CharField(max_length=50)
    difficulty = models.CharField(
        max_length=15,
        choices=
        [("Difficult","Difficult"),
        ("Simple","Simple")],
        # default="Simple",
    )
    objective = models.CharField(
         max_length=15,
        choices=
        [("Reminding","Reminding"),
        ("Understanding", "Understanding"),
        ("Creativity","Creativity")],
        default="Reminding",
    )
    courseID = models.ForeignKey(Course,on_delete=models.CASCADE)
    chapterNo = models.ForeignKey(Chapter,on_delete=models.CASCADE)

