from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Application(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=255)
    gender=models.CharField(max_length=12)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/images")
    Education_last=models.CharField(max_length=400)
    skills=models.TextField()
    achievements=models.TextField()
    def __str__(self):
        return self.user.username
