from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=200)
    total_question_added = models.IntegerField(default=0)