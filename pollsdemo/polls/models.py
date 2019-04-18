from django.db import models

# Create your models here.

class Options(models.Model):
    option = models.CharField(max_length=20)
    votes = models.IntegerField(max_length=255)
    oQuestion = models.ForeignKey('Questions',on_delete=models.CASCADE)

    def __str__(self):
        return self.option
    #更改后台列名显示
    def num(self):
        return self.votes
    num.short_description = "票数"

class Questions(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question