from django.db import models

# Create your models here.

class Options(models.Model):
    option = models.CharField(max_length=20)
    votes = models.IntegerField(max_length=255)
    oQuestion = models.ForeignKey('Questions',on_delete=models.CASCADE)

class Questions(models.Model):
    question = models.CharField(max_length=255)

