import datetime

from django.db import models
from django.utils import timezone

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'<Client: {self.name}>'


class Project(models.Model):
    name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)

    def __str__(self):
        return f'<Project: {self.name}>'


class HeroGeometry(models.Model):
    obj_name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)

    def __str__(self):
        return f'<HeroGeometry: {self.obj_name}>'


class BaseMap(models.Model):
    name = models.CharField(max_length=200)
    init_date = models.DateTimeField(timezone.now(), null=True)


    def __str__(self):
        return f'<HeroGeometry: {self.obj_name}>'



