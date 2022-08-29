from django.db import models
from user_api.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    option1 = models.CharField(max_length=50,null=False)
    option1_vote = models.IntegerField(default=0)
    option2 = models.CharField(max_length=50,null=False)
    option2_vote = models.IntegerField(default=0)
    option3 = models.CharField(max_length=50,null=False)
    option3_vote = models.IntegerField(default=0)
    option4 = models.CharField(max_length=50,null=False)
    option4_vote = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)