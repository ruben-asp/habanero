from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Questions(models.Model):
    choice_text = models.CharField(max_length=200)

class Answers(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
