from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
# title
# subject
# date - current
# user

SUBJECTS = [
	('TLE','TLE'),
	('MATH','Mathematics'),
	('ENGLISH','English'),
	('FILIPINO','Filipino'),
	('MAPEH','MAPEH'),
	('SCIENCE','Science'),
	('ESP','ESP'),
	('AP','Araling Panlipunan')
    ]

class Task(models.Model):

    title = models.CharField(max_length=100)
    page = models.CharField(max_length=40)
    subject = models.CharField(choices=SUBJECTS, max_length=50)
    week = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Schedule(models.Model):
    monday = MultiSelectField(choices=SUBJECTS)
    tuesday = MultiSelectField(choices=SUBJECTS)
    wednesday = MultiSelectField(choices=SUBJECTS)
    thursday = MultiSelectField(choices=SUBJECTS)
    friday = MultiSelectField(choices=SUBJECTS)
    saturday = MultiSelectField(choices=SUBJECTS)