from django.db import models

from django.contrib.auth.models import User

#upload -> course_title, instructor, semester, pdf
class Profile(models.Model):
    #file  
    profile_pic = models.ImageField(null=True, blank=True)
    #upload pdf file
    notes_pdf = models.FileField(null=True, blank=True)
    #course title
    course_title = models.CharField(max_length=255, null=True, blank=True)
    #instructor name
    instructor = models.CharField(max_length=255, null=True, blank=True)
    #semester
    semester = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

