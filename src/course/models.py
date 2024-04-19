from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    likes = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    urls = models.FileField(upload_to='notes/')
    description =models.TextField()    

    def __str__(self):
        return f"Course by {self.creator.username} with {self.likes} likes"
